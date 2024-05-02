# Data Ingestion and Transformation Using Amazon EMR and Apache Spark
## A. Task 1: Review and upload input data to Amazon S3
In this task, you review the Iris dataset and upload it to S3.

REQUIREMENTS AND CONFIGURATION
1. Choose the [iris_data](https://us-west-2-tcprod.s3.us-west-2.amazonaws.com/courses/SPL-TF-100-DEAFL1/v1.0.0.prod-cf6fd68f/scripts/iris_data.csv) link to download and save the dataset.
 Note: An S3 bucket, xxxx-labdatabucket-xxxx, has been created as part of the lab.

Upload the iris_data.csv to xxxx-labdatabucket-xxxx S3 bucket.
 Note: Hints and instructions are available in the [Appendix](https://labs.skillbuilder.aws/sa/lab/arn%3Aaws%3Alearningcontent%3Aus-east-1%3A470679935125%3Ablueprintversion%2FSPL-TF-100-DEAFL1-1%3A1.0.0-7a1500c5/en-US/27aa63be-6f00-43c7-b624-c32768d30634::mjVXbFvantSr3RSZ2YHdU6#task1-appendix) section if you need them.

 Task complete: You have successfully reviewed the data and uploaded it to the S3 bucket.

 ## B. Task 2: Connect to an EMR cluster using AWS CLI
In this task, you create an SSH connection to the EMR Cluster using the AWS CLI.

 Note: An EMR cluster has been created as part of the lab.

REQUIREMENTS AND CONFIGURATION
1. Copy the **CommandHostSessionManagementUrl** value listed to the left of these instructions, and then paste the value into a new web browser tab.
You will be redirected to the command host terminal.

 Note: Use AWS CLI commands from the instance to connect to the EMR cluster.

List the EMR clusters that are associated with your account, and get the EMR cluster ID.
 Learn more: Refer to [AWS CLI Command Reference: list-clusters](https://docs.aws.amazon.com/cli/latest/reference/emr/list-clusters.html) for more information about listing all active EMR clusters.

Use the EMR cluster ID to get the PublicDNS name of the EMR cluster.
 Learn more: Refer to [AWS CLI Command Reference: describe-cluster](https://docs.aws.amazon.com/cli/latest/reference/emr/describe-cluster.html) for more information about getting cluster level details for the given EMR cluster ID.

 Command: To SSH to the EMR cluster, run the following command:
 Note: Replace HOST with the MasterPublicDnsName value from the above output.

````sh
ssh -i ~/EMRKey.pem hadoop@HOST
````

 Learn more: Refer to [AWS CLI Command Reference: ssh](https://docs.aws.amazon.com/cli/latest/reference/emr/ssh.html) for more information about how to SSH into the master node of the cluster.

Enter yes at the prompt.
The EMR terminal displays.

 Note: Hints and instructions are available in the [Appendix](https://labs.skillbuilder.aws/sa/lab/arn%3Aaws%3Alearningcontent%3Aus-east-1%3A470679935125%3Ablueprintversion%2FSPL-TF-100-DEAFL1-1%3A1.0.0-7a1500c5/en-US/27aa63be-6f00-43c7-b624-c32768d30634::mjVXbFvantSr3RSZ2YHdU6#task2-appendix) section if you need them.

 Task complete: You have successfully connected to the EMR cluster using the AWS CLI.