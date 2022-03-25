import fileinput
import os

from flask import current_app
from google.cloud import storage
from src.utils import constants


class GoogleCloudStorage:
    def __init__(self, project) -> None:
        self.project = project
        self.storage_client = storage.Client(project=self.project)

    def add_bucket_iam_member(self, bucket_name, role, member):
        """Add a new member to an IAM Policy"""
        # bucket_name = "your-bucket-name"
        # role = "IAM role, e.g., roles/storage.objectViewer"
        # member = "IAM identity, e.g., user: name@example.com"

        bucket = self.storage_client.bucket(bucket_name)
        policy = bucket.get_iam_policy(requested_policy_version=3)
        policy.bindings.append({"role": role, "members": {member}})
        bucket.set_iam_policy(policy)
        print(f"Added {member} with role {role} to {bucket_name}.")

    def copy_parameters_to_bucket(self, study_title, role, bucket_name: str = constants.PARAMETER_BUCKET):
        bucket = self.storage_client.bucket(bucket_name)
        for filename in constants.PARAMETER_FILES:
            blob = bucket.blob(filename)
            blob.download_to_filename(os.path.join(constants.TEMP_FOLDER, filename))
            self.update_parameters(os.path.join(constants.TEMP_FOLDER, filename), study_title, role)
            blob.upload_from_filename(os.path.join(constants.TEMP_FOLDER, filename))
        print(f"Updated parameters in {constants.PARAMETER_FILES}")

    def update_parameters(self, file, study_title, role):
        db = (
            current_app.config["DATABASE"]
            .collection("studies")
            .document(study_title.replace(" ", "").lower())
            .get()
            .to_dict()
        )
        pars = db["parameters"]

        if role == file.split(".")[-2]:
            pars = pars | db["personal_parameters"][db["participants"][int(role) - 1]]

        pars["NUM_INDS_SP_1"] = db["personal_parameters"][db["participants"][0]]["NUM_INDS"]
        pars["NUM_INDS_SP_2"] = db["personal_parameters"][db["participants"][1]]["NUM_INDS"]
        pars["NUM_INDS"] = {"value": ""}
        pars["NUM_INDS"]["value"] = str(int(pars["NUM_INDS_SP_1"]["value"]) + int(pars["NUM_INDS_SP_2"]["value"]))

        for line in fileinput.input(file, inplace=True):
            key = str(line).split(" ")[0]
            if key in pars:
                line = f"{key} " + str(pars[key]["value"]) + "\n"
            print(line, end="")

    def upload_to_bucket(self, file, filename, bucket_name: str = constants.PARAMETER_BUCKET):
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(filename)
        blob.upload_from_file(file)
        print(f"Uploaded {filename} to bucket")

    def check_file_exists(self, filename, bucket_name: str = constants.PARAMETER_BUCKET):
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(filename)
        return blob.name in [b.name for b in bucket.list_blobs()]
