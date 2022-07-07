#!/usr/bin/env python3

#import all required python libraries
import boto3
import json
import subprocess
import csv
import sys
from pprint import pprint as pp
from boto3 import Session

wsclient = boto3.client('workspaces', region_name='us-east-1')

region = "us-east-1"

client = boto3.client('workspaces', region_name=region)

workspaces = client.describe_workspaces()['Workspaces']

#Operation selection menu
print("\n"+"Select the operation you want to perform on the workspace: ")

print("\n"+"0 -> if you want to DESCRIBE properties of a workspace"+"\n")

print("1 -> if you want to START a workspace"+"\n")

print("2 -> if your want to STOP a workspace"+"\n")

print("3 -> if you want to REBOOT a workspace"+"\n")

print("4 -> if you want to MODIFY a workspace"+"\n")

print("5 -> if you want to TERMINATE a workspace"+"\n")

print("6 -> if you want to get all workspaces properties residing in an environment in a csv file"+"\n")   

#Selected operation 
selected_option = raw_input("\n"+"Now please enter the number corresponding to operation you want to perform on the workspace: " )

print("\n"+"You have selected option number:"+selected_option)

#print(type(selected_option))

selected_option = int(selected_option)

#print(type(selected_option))

#Depending on the selected operation corresponding python script will execute
if selected_option == 0:
  execfile("describe_workspaces.py")
elif selected_option == 1:
  execfile("start_workspaces.py")
elif selected_option == 2:
  execfile("stop_workspaces.py")
elif selected_option == 3:
  execfile("reboot_workspaces.py")
elif selected_option == 4:
  execfile("modify_workspaces.py")
elif selected_option == 5:
  execfile("terminate_workspaces.py")
elif selected_option == 6:
  execfile("get_all__workspaces_properties.py")
else: 
  print("\n"+"You have entered an invalid input, program will now exit")
  exit()
