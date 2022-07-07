#!/usr/bin/env python3

import boto3
import json
import csv
import sys
from pprint import pprint as pp
from boto3 import Session
from datetime import datetime

wsclient = boto3.client('workspaces', region_name='us-east-1')

region = "us-east-1"

client = boto3.client('workspaces', region_name=region)

workspaces = client.describe_workspaces()['Workspaces']

directory_id = raw_input("\n"+"Enter the Directory ID of the workspace you want to CREATE: ")

username = raw_input("\n"+"Enter the Username of the user for whom you want to CREATE this workspace: ")

bundle_id = raw_input("\n"+"Enter the Bundle ID of the workspace you want to CREATE: ")

user_volume_encryption = raw_input("\n"+"Do you want to enable User Volume Encryption for this workspace??(Answer True or False): ")

user_volume_encryption = json.loads(user_volume_encryption.lower())

##print(type(user_volume_encryption))

root_volume_encryption = raw_input("\n"+"Do you want to enable Root Volume Encryption for this workspace??(Answer True or False): ")

root_volume_encryption = json.loads(root_volume_encryption.lower())

##print(type(root_volume_encryption))

volume_encryption_key = raw_input("\n"+"Enter the Volume Encryption Key of the workspace you want to CREATE: ")

running_mode = raw_input("\n"+"Please specify the running mode for this workspace??(Answer should be either AUTO_STOP or ALWAYS_ON): ")

auto_stop_time_out = raw_input("\n"+"Please specify the auto stop timeout for this workspace(Answer should be 0,60,120): ")

auto_stop_time_out = int(auto_stop_time_out)

root_volume_size = raw_input("\n"+"Please specify the root volume size for this workspace(Answer should be +ve integer): ")

root_volume_size = int(root_volume_size)

user_volume_size = raw_input("\n"+"Please specify the user volume size for this workspace(Answer should be +ve integer): ")

user_volume_size = int(user_volume_size)

compute_type_name = raw_input("\n"+"Please specify the compute type for this workspace(Answer should be 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'): ")

workspace_requester_username = raw_input("\n"+"Please specify the username of the requester for this workspace: ")

now = datetime.now()

workspace_creation_date_time = now.strftime("%d/%m/%Y %H:%M:%S")

workspace_environment = raw_input("\n"+"Please specify the environment in which this workspace is being provisioned: ")

response = client.create_workspaces(
    Workspaces=[
        {
            'DirectoryId': directory_id,
            'UserName': username,
            'BundleId': bundle_id,
            'VolumeEncryptionKey': volume_encryption_key ,
            'UserVolumeEncryptionEnabled': user_volume_encryption,
            'RootVolumeEncryptionEnabled': root_volume_encryption,
            'WorkspaceProperties': {
                'RunningMode': running_mode,
                'RunningModeAutoStopTimeoutInMinutes': auto_stop_time_out,
                'RootVolumeSizeGib': root_volume_size,
                'UserVolumeSizeGib': user_volume_size,
                'ComputeTypeName': compute_type_name
            },
            'Tags': [
                {
                    'Key': 'requester',
                    'Value': workspace_requester_username,
                    'Key': 'createdOn',
                    'Value': workspace_creation_date_time,
                    'Key': 'env',
                    'Value': workspace_environment
                },
            ]
        },
    ]
)


#workspaces_info = [{"id":workspace['WorkspaceId'], "ip": workspace['IpAddress'], "user": workspace['UserName'], "state": workspace['State']} for workspace in workspaces]
#pp(workspaces_info)

print(response)


status_code = response.get('ResponseMetadata').get('HTTPStatusCode')

if status_code == 200:
  print("\n"+"Workspace CREATION has been initiated successfully,please wait for approx 45 mins to 1 Hour for it to complete") 
else:
  print("\n"+"Workspace hasn't been able to provision successfully,please provision it from the aws console")
