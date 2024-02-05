#!/bin/bash

# Create user with attached iam policy and provide credentials in aws profile

aws --profile spot-pricing ec2 describe-spot-price-history \
    --instance-types t2.micro t2.medium m6g.xlarge m6g.2xlarge m6g.4xlarge c4.large c4.xlarge c4.2xlarge c4.4xlarge r4.large r4.xlarge r4.2xlarge r4.4xlarge \
    --product-descriptions="Linux/UNIX" \
    --region "us-east-1"

aws --profile spot-pricing ec2 describe-spot-price-history \
    --instance-types t2.micro t2.medium m6g.xlarge m6g.2xlarge m6g.4xlarge c4.large c4.xlarge c4.2xlarge c4.4xlarge r4.large r4.xlarge r4.2xlarge r4.4xlarge \
    --product-descriptions="Linux/UNIX" \
    --region "us-east-2"