import pytest
from utils.recorder import TestRecorder
from utils.dummy_driver import DummyWebDriver
from utils.profile import update_profile

profiles = ["ok", "newname", "crash", "avatar"]

CASES = []
for i in range(1, 351):
    CASES.append({
        "tc_id": f"TC_PROFILE_{i:04}",
        "name": f"test_profile_{i:04}",
        "module": "module_profile",
        "file": "tests/module_profile/test_profile.py",
        "profile": profiles[i % len(profiles)]
    })

@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_profile(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open profile page")
    drv = DummyWebDriver()

    recorder.step("Step 2: Update profile")
    update_profile(data["profile"])
