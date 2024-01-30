#!/bin/bash

# Check if the S3 bucket exists
aws s3api head-bucket --bucket rcodebucket

# If it doesn't exist, create the bucket
if [ $? -ne 0 ]; then
  aws s3api create-bucket --bucket rcodebucket --region us-west-1
  aws s3api put-object --bucket rcodebucket --key test.txt --body /path/to/test.txt
fi

# Create EC2-Admin group and attach inline policy
aws iam create-group --group-name EC2-Admin
echo '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    }
  ]
}' > ec2-admin-inline-policy.json
aws iam put-group-policy --group-name EC2-Admin --policy-name EC2-Admin-Inline-Policy --policy-document file://ec2-admin-inline-policy.json

# Create EC2-Support group and attach AmazonEC2ReadOnlyAccess managed policy
aws iam create-group --group-name EC2-Support
aws iam attach-group-policy --group-name EC2-Support --policy-arn arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess

# Create S3-Support group and attach AmazonS3ReadOnlyAccess managed policy
aws iam create-group --group-name S3-Support
aws iam attach-group-policy --group-name S3-Support --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# Create user-1 and add to S3-Support group
aws iam create-user --user-name user-1
aws iam create-login-profile --user-name user-1 --password solarwinds
aws iam add-user-to-group --user-name user-1 --group-name S3-Support

# Create user-2 and add to EC2-Support group
aws iam create-user --user-name user-2
aws iam create-login-profile --user-name user-2 --password solarwinds
aws iam add-user-to-group --user-name user-2 --group-name EC2-Support

# Create user-3 and add to EC2-Admin group
aws iam create-user --user-name user-3
aws iam create-login-profile --user-name user-3 --password solarwinds
aws iam add-user-to-group --user-name user-3 --group-name EC2-Admin
