#!/usr/bin/env python3

import boto3
import json
import csv
import sys
from pprint import pprint as pp
from boto3 import Session


wsclient = boto3.client('workspaces', region_name='us-east-1')

region = "us-east-1"

client = boto3.client('workspaces', region_name=region)

workspaces = client.describe_workspaces()['Workspaces']

workspace_id = raw_input("\n"+"Enter the workspace id of the workspace you want to MODIFY: ")

print("\n"+"Please specify the workspace properties in the below questions:")

running_mode = raw_input("\n"+"Enter the running mode of the workspace(please specify AUTO_STOP or ALWAYS_ON): ")

auto_stop_time_out = raw_input("\n"+"Enter the auto stop time out of the workspace(please specify in 60-minute(s) interval): ")

root_volume_size = raw_input("\n"+"Enter the new size of the root volume(has to be an allowed integer value): ")

user_volume_size = raw_input("\n"+"Enter the new size of the user volume(has to be an allowed integer value): ")
 
compute_type_name = raw_input("\n"+"Enter the new compute type of the workspace(please specify 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'POWERPRO): ")

response = client.modify_workspace_properties(
    WorkspaceId=workspace_id,
    WorkspaceProperties={
        'RunningMode': running_mode,
        'RunningModeAutoStopTimeoutInMinutes': auto_stop_time_out,
        'RootVolumeSizeGib': root_volume_size,
        'UserVolumeSizeGib': user_volume_size,
        'ComputeTypeName': compute_type_name
    }
)


#workspaces_info = [{"id":workspace['WorkspaceId'], "ip": workspace['IpAddress'], "user": workspace['UserName'], "state": workspace['State']} for workspace in workspaces]
#pp(workspaces_info)

##print(response)

status_code = response.get('ResponseMetadata').get('HTTPStatusCode')

if status_code == 200:
  print("\n"+"Workspace UPDATE has been initiated successfully, please wait for an hour  for it to complete") 
else:
  print("\n"+"Workspace hasn't been able to update  successfully,please update it from the aws console")
