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

workspace_id = raw_input("\n"+"Enter the workspace id of the workspace you want to STOP: ")

response = client.stop_workspaces(
    StopWorkspaceRequests=[
        {
            'WorkspaceId': workspace_id
        },
    ]
)


#workspaces_info = [{"id":workspace['WorkspaceId'], "ip": workspace['IpAddress'], "user": workspace['UserName'], "state": workspace['State']} for workspace in workspaces]
#pp(workspaces_info)

##print(response)

status_code = response.get('ResponseMetadata').get('HTTPStatusCode')

if status_code == 200:
  print("\n"+"Workspace STOP has been initiated successfully, please wait for couple of minutes for it to complete") 
else:
  print("\n"+"Workspace hasn't been able to stopped successfully,please STOP it from the aws console")
