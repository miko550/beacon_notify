# Microsoft Teams Beacon Notify
New beacon notifications in Cobalt Strike for Microsoft Teams
AggressorScript and python script to notify you via Microsoft Teams when a new beacon checks in.

## Installation
1. Setup and get Microsoft Teams webhook. [reference](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet)
2. Copy the webhook url and paste it in alert.py in the webhookurl variable.
3. Edit ms_teams_notify.cna and replace the "path_to_py" variable with the path to the alert.py file.
4. Load the .cna file in the teamserver via the headless AggressorScript console ./agscript
5. Remember to leave the agscript instance running, can use linux "screen" utility.

### Example
```
./agscript {host and creds etc}
aggressor> load {path to discord_notify.cna}
ctrl^a+d
*exited screen*
exit
```

## Reference
- https://github.com/CodeXTF2/beacon_notify_discordhook
- https://threatexpress.com/blogs/2016/slack-notifications-for-cobalt-strike/
- https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet
