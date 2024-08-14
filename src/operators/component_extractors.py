from dateutil.parser import isoparse
import human_readable


def get_status(payload: dict) -> bool | None:
    return payload.get("status")


def get_repo(payload: dict) -> str:
    return payload.get("substitutions", {}).get("_REPO_NAME")


def get_branch(payload: dict) -> str:
    return payload.get("substitutions", {}).get("BRANCH_NAME")


def get_project_id(payload: dict) -> str | None:
    return payload.get("projectId")


def get_duration(payload: dict) -> str:
    human_readable.i18n.activate("en_ABBR")
    time_start: str = payload.get("timing", {}).get("FETCHSOURCE", {}).get("startTime")
    time_end: str = payload.get("timing", {}).get("BUILD", {}).get("endTime")
    if time_start is None or time_end is None:
        return "n/a"
    duration_str: str = human_readable.precise_delta(
        isoparse(time_end) - isoparse(time_start)
    )
    return duration_str


def get_build_url(payload: dict) -> str | None:
    return payload.get("logUrl")
