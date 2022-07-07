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

workspace_id = raw_input("\n"+"Enter the workspace id of the workspace whose properties you want to know : ")

response = client.describe_workspaces(
    WorkspaceIds=[
        workspace_id,
    ]
)


#workspaces_info = [{"id":workspace['WorkspaceId'], "ip": workspace['IpAddress'], "user": workspace['UserName'], "state": workspace['State']} for workspace in workspaces]
#pp(workspaces_info)

print(response)

print("\n"+"Username: "+response.get('Workspaces')[0].get('UserName')+"\n")

print("IPAddress: "+response.get('Workspaces')[0].get('IpAddress')+"\n")

print("Workspace_State: "+response.get('Workspaces')[0].get('State')+"\n")

print("Workspace_ComputeType: "+response.get('Workspaces')[0].get('WorkspaceProperties').get('ComputeTypeName')+"\n")

print("Workspace_RunningMode: "+response.get('Workspaces')[0].get('WorkspaceProperties').get('RunningMode')+"\n")

print("Workspace_UserVolumeSize(in GB): "+str(response.get('Workspaces')[0].get('WorkspaceProperties').get('UserVolumeSizeGib'))+"\n")

print("Workspace_RootVolumeSize(in GB): "+str(response.get('Workspaces')[0].get('WorkspaceProperties').get('RootVolumeSizeGib'))+"\n")

status_code = response.get('ResponseMetadata').get('HTTPStatusCode')

if status_code == 200:
  print("^^^Workspace properties have been described above^^^"+"\n") 
else:
  print("Workspace properties couldn't be displayed right now ,please do  it from the aws console")
