
import os
import sys

from flask import Flask, redirect, render_template, request, url_for
from waitress import serve

import global_variables
from utils.google_cloud.google_cloud_compute import GoogleCloudCompute
from utils.google_cloud.google_cloud_pubsub import GoogleCloudPubsub
from utils.google_cloud.google_cloud_storage import GoogleCloudStorage

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('home.html', project=global_variables.SERVER_PROJECT)
    elif request.method == 'POST':
        role: str = request.form['role']
        global_variables.CLIENT_PROJECT = request.form['project']

        gcloudCompute = GoogleCloudCompute(global_variables.CLIENT_PROJECT)
        gcloudStorage = GoogleCloudStorage(global_variables.SERVER_PROJECT)
        gcloudPubsub = GoogleCloudPubsub(global_variables.SERVER_PROJECT, role)

        gcloudPubsub.create_topic_and_subscribe()

        instance = global_variables.INSTANCE_NAME_ROOT + role

        gcloudCompute.validate_networking()

        vm_external_ip_address = gcloudCompute.setup_instance(global_variables.ZONE, instance)

        # Give instance publish access to pubsub for status updates
        member = "serviceAccount:" + \
            gcloudCompute.get_service_account_for_vm(
                zone=global_variables.ZONE, instance=instance)
        gcloudPubsub.add_pub_iam_member("roles/pubsub.publisher", member)

        # Create bucket to store the ip addresses; this will be read-only for the VMs
        bucket = gcloudStorage.validate_bucket(role)
        blob = bucket.blob("ip_addresses/P" + role)
        blob.upload_from_string(vm_external_ip_address)

        # Give the instance's service account read-access to this bucket
        gcloudStorage.add_bucket_iam_member(
            global_variables.BUCKET_NAME, "roles/storage.objectViewer", member)

        print("I've done what I can.  GWAS should be running now.")
        return redirect(url_for("running", role=role))


@app.route("/running/<role>", methods=['GET', 'POST'])
def running(role):
    gcloudPubsub = GoogleCloudPubsub(global_variables.SERVER_PROJECT, role)
    gcloudCompute = GoogleCloudCompute(global_variables.CLIENT_PROJECT)
    gcloudPubsub.listen_to_startup_script()
    
    if global_variables.STATUS.split(" ")[0] == "GWAS_completed":
        gcloudCompute.stop_instance(global_variables.ZONE, global_variables.INSTANCE_NAME_ROOT + role)
        return "GWAS completed; yay!"
    
    return render_template('running.html', status=global_variables.STATUS)


if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else 5000
    serve(app, port=p)
