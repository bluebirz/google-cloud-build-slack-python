import requests


def send_slack(url: str, message: str) -> None:
    # print(url)
    # print(message)
    response: requests.Response = requests.post(
        url=url,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        json=message,
    )
    print(response.status_code, response.text)
