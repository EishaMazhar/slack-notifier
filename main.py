import json
import sys
import requests

if __name__ == "__main__":
    url = "https://hooks.slack.com/services/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"
    message = "A Sample message by bot"
    title = "test"
    slack_data = {"username": "slack-bot",
                  "icon_emoji": ":satellite:",
                  "channel": "general",
                  "attachments": [
                      {
                          "color": " # 9737EE",
                          "fields": [
                              {
                                  "title": title,
                                  "value": message,
                                  "short": "false",
                              }
                          ]},
                  ]}
    byte_length = str(sys.getsizeof(slack_data))
    headers = {"Content - Type": "application / json", "Content - Length": byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
