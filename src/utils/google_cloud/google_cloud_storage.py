import fileinput
import time

from flask import current_app
from google.cloud import storage
from src import constants


class GoogleCloudStorage:
    def __init__(self, project) -> None:
        self.project = project
        self.storage_client = storage.Client(project=self.project)

    def validate_bucket(self, role):
        buckets_list = [bucket.name for bucket in self.storage_client.list_buckets()]

        if constants.BUCKET_NAME not in buckets_list:
            print(f"Creating bucket {constants.BUCKET_NAME}")
            self.storage_client.create_bucket(constants.BUCKET_NAME)
            time.sleep(1)

        self.delete_blob(constants.BUCKET_NAME, "ip_addresses/IP_ADDR_P" + role)

        return self.storage_client.bucket(constants.BUCKET_NAME)

    def add_bucket_iam_member(self, bucket_name, role, member):
        """Add a new member to an IAM Policy"""
        # bucket_name = "your-bucket-name"
        # role = "IAM role, e.g., roles/storage.objectViewer"
        # member = "IAM identity, e.g., user: name@example.com"

        bucket = self.storage_client.bucket(bucket_name)
        policy = bucket.get_iam_policy(requested_policy_version=3)
        policy.bindings.append({"role": role, "members": {member}})
        bucket.set_iam_policy(policy)
        print("Added {} with role {} to {}.".format(member, role, bucket_name))

    def delete_blob(self, bucket_name, blob_name):
        """Deletes a blob from the bucket."""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        if blob.name in [b.name for b in bucket.list_blobs()]:
            blob.delete()
            print("Blob {} deleted.".format(blob_name))
        else:
            print(f"Blob {blob_name} didn't exist")

    def copy_parameters_to_bucket(self, project_title):
        bucket = self.storage_client.bucket(constants.BUCKET_NAME)
        for file in constants.PARAMETER_FILES:
            blob = bucket.blob(file)
            blob.download_to_filename(file)
            self.update_parameters(file, project_title)
            blob.upload_from_filename(file)
            print(f"Updated parameters in {file}")

    def update_parameters(self, file, project_title):
        db = current_app.config["DATABASE"]
        parameters = (
            db.collection("projects")
            .document(project_title)
            .get()
            .to_dict()["parameters"]
        )

        for line in fileinput.input(file, inplace=True):
            key = line.split(" ")[0]
            if key in parameters:
                line = key + " " + str(parameters[key]["value"]) + "\n"
            print(line, end="")
