#!/usr/bin/env python3

#import all required python libraries
import boto3
import json

#aws environment selection commands
print("\n"+"Type the following commands in your shell to switch to a specific aws environment:- "+"\n")

print("If you want to SWITCH to CBSC-DEV environment please execute this command : export AWS_PROFILE=cbsc_dev "+"\n")

print("If your want to SWITCH to CBSC-QAT environment please execute this command : export AWS_PROFILE=cbsc_qat"+"\n")

print("If you want to SWITCH to CBSC-PROD environment please execute this command : export AWS_PROFILE=cbsc_prod"+"\n")

exit()
