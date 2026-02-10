import pytest
from utils.recorder import TestRecorder
from utils.dummy_driver import DummyWebDriver
from utils.player import play

videos = ["ok", "age", "network", "format", "codec", "ok"]

CASES = []
for i in range(1, 351):
    CASES.append({
        "tc_id": f"TC_PLAYER_{i:04}",
        "name": f"test_player_{i:04}",
        "module": "module_player",
        "file": "tests/module_player/test_player.py",
        "video": videos[i % len(videos)]
    })

@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_player(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open video")
    drv = DummyWebDriver()

    recorder.step("Step 2: Play video")
    play(data["video"])
