import json
from src.operators.component_extractors import (
    get_branch,
    get_build_url,
    get_duration,
    get_project_id,
    get_repo,
    get_status,
)
import unittest


class TestMessageExtraction(unittest.TestCase):
    def setUp(self):
        filepath = "tests/sample-payload.json"
        with open(filepath, "r") as fptr:
            self.mock_payload = json.load(fptr)
        # print(self.mock_payload)

    def test_get_status(self):
        assert get_status(self.mock_payload) == "FAILURE"

    def test_get_repo(self):
        assert get_repo(self.mock_payload) == "google-cloud-build-slack-python"

    def test_get_branch(self):
        assert get_branch(self.mock_payload) == "dev"

    def test_get_project_id(self):
        assert get_project_id(self.mock_payload) == "bluebirz-playground"

    def test_get_duration(self):
        assert get_duration(self.mock_payload) == "7.48s"

    def test_get_build_url(self):
        assert (
            get_build_url(self.mock_payload)
            == "https://console.cloud.google.com/cloud-build/builds/05fde482-f5d0-46f2-b5e7-246055b83134?project=1234"
        )


if __name__ == "__main__":
    unittest.main()
