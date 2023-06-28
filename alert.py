import requests
import argparse

parser = argparse.ArgumentParser(description='beacon info')
parser.add_argument('--username')
parser.add_argument('--computername')
parser.add_argument('--externalip')
parser.add_argument('--internalip')
parser.add_argument('--arch')

args = parser.parse_args()

user = args.username
computer = args.computername
external = args.externalip
internal = args.internalip
arch = args.arch

message = "**New Beacon!** \n\n Username : {} \n\n Computer Name : {} \n\n External IP : {} \n\n Internal IP : {} \n\n Arch : {}".format(user,computer,external,internal,arch)
 
adaptiveCardJson = {
  "type": "TextBlock",
  "text": message
}

webhookUrl = "https://xxxxx.webhook.office.com/xxxxxx"

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhookUrl, headers=headers, json=adaptiveCardJson)

# print(response.status_code)
# print(response.text)
