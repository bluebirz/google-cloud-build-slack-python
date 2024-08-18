import requests
import json


def send_slack(url: str, message: str) -> None:
    response: requests.Response = requests.post(
        url=url,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        json=json.loads(message),
    )
    print(response.status_code, response.text)
    if response.status_code != 200:
        print(message)
