import json

user_volume_encryption = raw_input("\n"+"Do you want to enable User Volume Encryption for this workspace??(Answer True or False): ")

user_volume_encryption = json.loads(user_volume_encryption.lower())

print(type(user_volume_encryption))

root_volume_encryption = raw_input("\n"+"Do you want to enable Root Volume Encryption for this workspace??(Answer True or False): ")


root_volume_encryption = json.loads(root_volume_encryption.lower())

print(type(root_volume_encryption))
