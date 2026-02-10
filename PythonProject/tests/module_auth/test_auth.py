import pytest
from utils.recorder import TestRecorder
from utils.dummy_driver import DummyWebDriver
from utils.auth import login

CASES = []
for i in range(1, 351):
    CASES.append({
        "tc_id": f"TC_AUTH_{i:04}",
        "name": f"test_auth_{i:04}",
        "module": "module_auth",
        "file": "tests/module_auth/test_auth.py",
        "user": "bad_user" if i % 4 == 0 else "good_user"
    })

@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_auth(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open login page")
    drv = DummyWebDriver()

    recorder.step("Step 2: Attempt login")
    login(data["user"])
