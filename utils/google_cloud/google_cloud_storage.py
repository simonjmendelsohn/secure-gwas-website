
import time

import global_variables
from google.cloud import storage


class GoogleCloudStorage():

    def __init__(self, project) -> None:
        self.project = project
        self.storage_client = storage.Client(project=self.project)

    def validate_bucket(self, role):
        buckets_list = [
            bucket.name for bucket in self.storage_client.list_buckets()]

        if global_variables.BUCKET_NAME not in buckets_list:
            print(f"Creating bucket {global_variables.BUCKET_NAME}")
            self.storage_client.create_bucket(global_variables.BUCKET_NAME)
            time.sleep(1)

        self.delete_blob(global_variables.BUCKET_NAME,
                         "ip_addresses/IP_ADDR_P" + role)

        return self.storage_client.bucket(global_variables.BUCKET_NAME)

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
