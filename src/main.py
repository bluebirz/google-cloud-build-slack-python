import base64
import json
import os

from jinja2 import Template

from operators.component_extractors import (
    get_branch,
    get_build_url,
    get_duration,
    get_project_id,
    get_repo,
    get_status,
)
from operators.slack_sender import send_slack

SLACK_URL = os.environ.get("SLACK_URL")
STATUS_TEMPLATE_MAPPING = {
    "SUCCESS": "templates/template_success.j2",
    "FAILURE": "templates/template_failed.j2",
}


def create_message(message: dict) -> str:
    status: str = get_status(payload=message)
    template_file: str | None = STATUS_TEMPLATE_MAPPING.get(status)

    if template_file is None:
        print(
            f"skip this status: {status}. Must be any of {STATUS_TEMPLATE_MAPPING.keys()}"
        )
        return None
    with open(template_file, "r") as fptr:
        template: str = fptr.read()

    slack_payload: str = Template(template).render(
        repo=get_repo(payload=message),
        branch=get_branch(payload=message),
        project_id=get_project_id(payload=message),
        duration=get_duration(payload=message),
        url=get_build_url(payload=message),
    )
    return slack_payload


def cloudbuild_notifications(event, context):
    if SLACK_URL is None:
        raise ValueError("Require SLACK_URL")
    message: dict = json.loads(base64.b64decode(event.get("data")).decode("utf-8"))
    slack_msg: str = create_message(
        message=message,
    )
    if slack_msg is not None:
        send_slack(url=SLACK_URL, message=slack_msg)
