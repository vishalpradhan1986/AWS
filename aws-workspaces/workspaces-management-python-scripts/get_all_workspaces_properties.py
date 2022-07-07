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


paginator = wsclient.get_paginator('describe_workspaces')

pages = paginator.paginate()

ws_found = False

'''
{u'BundleId': u'wsb-hztzqyk3m',
  u'ComputerName': u'WSAMZN-S23S24EN',
  u'DirectoryId': u'd-90671ca14c',
  u'IpAddress': u'10.130.5.213',
  u'ModificationStates': [],
  u'RootVolumeEncryptionEnabled': True,
  u'State': u'AVAILABLE',
  u'SubnetId': u'subnet-0763e4d03c0f42ef8',
  u'UserName': u'renga.shunmuga',
  u'UserVolumeEncryptionEnabled': True,
  u'VolumeEncryptionKey': u'arn:aws:kms:us-east-1:687115541366:key/703f8466-edc7-4f97-b4fd-d60f5008f9be',
  u'WorkspaceId': u'ws-gn1rhgrnf',
  u'WorkspaceProperties': {u'ComputeTypeName': u'PERFORMANCE',
                           u'RootVolumeSizeGib': 80,
                           u'RunningMode': u'ALWAYS_ON',
                           u'UserVolumeSizeGib': 50}}
'''

workspaces_info = [{"id":workspace['WorkspaceId'], "ip": workspace['IpAddress'], "user": workspace['UserName'], "state": workspace['State']} for workspace in workspaces]
pp(workspaces_info)

# field names
fields = ['UserName', 'ComputerName', 'WorkspaceId', 'IpAddress', 'State']
filename = "workspaces_properties.csv"
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    for page in pages:
        for workspace in page['Workspaces']:
            # writing the data rows
            rows = [
                [workspace['UserName'],
                workspace['ComputerName'],
                workspace['WorkspaceId'],
                workspace['IpAddress'],
                workspace['State']],
            ]
            csvwriter.writerows(rows)

