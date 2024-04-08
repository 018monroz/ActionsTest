import requests
import json

url = "https://api.github.com/repos/018monroz/ActionsTest/actions/workflows/manual.yml/dispatches"
token = ""

payload = json.dumps({
  "ref": "main",
  "inputs": {
    "name": "Nequi",
    "file": "test"
  }
})
headers = {
  'Accept': 'application/vnd.github+json',
  'Authorization': 'Bearer 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',
  'X-GitHub-Api-Version': '2022-11-28',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
