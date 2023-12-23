# A Day in the Life of a Data Engineer

- [A Day in the Life of a Data Engineer](#a-day-in-the-life-of-a-data-engineer)
  - [Task 1: Create and run an AWS Glue crawler](#task-1-create-and-run-an-aws-glue-crawler)
  - [Task 2: Review the IAM policies](#task-2-review-the-iam-policies)
  - [Task 3: View the table in the Data Catalog](#task-3-view-the-table-in-the-data-catalog)
  - [Task 4: Run a job in AWS Glue Studio to transform the data](#task-4-run-a-job-in-aws-glue-studio-to-transform-the-data)
  - [Task 5: Query the data\_parquet table in Amazon Athena](#task-5-query-the-data_parquet-table-in-amazon-athena)


## Task 1: Create and run an AWS Glue crawler

## Task 2: Review the IAM policies
This lab policy provides ``Amazon S3`` with read and write access to the lab environment’s S3 buckets. The ``AWS Glue`` job that you created requires these privileges because it reads and writes information to ``Amazon S3`` while processing data.

````JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:AbortMultipartUpload",
                "s3:DeleteObject",
                "s3:DeleteObjectTagging",
                "s3:DeleteObjectVersion",
                "s3:DeleteObjectVersionTagging",
                "s3:Describe*",
                "s3:Get*",
                "s3:List*",
                "s3:PutAnalytics*",
                "s3:PutBucketAcl",
                "s3:PutBucketCORS",
                "s3:PutBucketLogging",
                "s3:PutBucketNotification",
                "s3:PutBucketPolicy",
                "s3:PutBucketTagging",
                "s3:PutBucketVersioning",
                "s3:PutBucketWebsite",
                "s3:PutEncryptionConfiguration",
                "s3:PutInventoryConfiguration",
                "s3:PutMetricsConfiguration",
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:PutObjectTagging",
                "s3:PutObjectVersionTagging"
            ],
            "Resource": [
                "arn:aws:s3:::query-result-c5748ad0",
                "arn:aws:s3:::glue-bucket-c5748ad0",
                "arn:aws:s3:::query-result-*/*",
                "arn:aws:s3:::glue-bucket-*/*"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "s3:Describe*",
                "s3:Get*",
                "s3:List*"
            ],
            "Resource": [
                "arn:aws:s3:::aws-tc-largeobjects/SPL-TF-200-ANGLUE-1/data/",
                "arn:aws:s3:::aws-tc-largeobjects/SPL-TF-200-ANGLUE-1/data/*"
            ],
            "Effect": "Allow"
        }
    ]
}
````

This lab policy gives ``AWS Glue`` access to related services such as ``Amazon Elastic Compute Cloud (Amazon EC2), Amazon S3, and Amazon CloudWatch Logs``. With these privileges, ``AWS Glue`` can read, write, and process data. It can also write information to ``Amazon CloudWatch`` logs.

````JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "glue:*",
                "s3:GetBucketLocation",
                "s3:ListBucket",
                "s3:ListAllMyBuckets",
                "s3:GetBucketAcl",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeRouteTables",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcAttribute",
                "iam:ListRolePolicies",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "cloudwatch:PutMetricData"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket"
            ],
            "Resource": [
                "arn:aws:s3:::aws-glue-*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::aws-glue-*/*",
                "arn:aws:s3:::*/*aws-glue-*/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::crawler-public*",
                "arn:aws:s3:::aws-glue-*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:*:*:*:/aws-glue/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags",
                "ec2:DeleteTags"
            ],
            "Condition": {
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": [
                        "aws-glue-service-resource"
                    ]
                }
            },
            "Resource": [
                "arn:aws:ec2:*:*:network-interface/*",
                "arn:aws:ec2:*:*:security-group/*",
                "arn:aws:ec2:*:*:instance/*"
            ]
        }
    ]
}
````
## Task 3: View the table in the Data Catalog

## Task 4: Run a job in AWS Glue Studio to transform the data
* [Why is the AWS Glue Crawler Running for a Long Time?](https://aws.amazon.com/premiumsupport/knowledge-center/long-running-glue-crawler/)
* [Best Practices to Optimize Cost and Performance for AWS Glue Streaming ETL Jobs](https://aws.amazon.com/blogs/big-data/best-practices-to-optimize-cost-and-performance-for-aws-glue-streaming-etl-jobs/)

## Task 5: Query the data_parquet table in Amazon Athena