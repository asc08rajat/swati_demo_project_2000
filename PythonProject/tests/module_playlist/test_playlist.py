import pytest
from utils.recorder import TestRecorder
from utils.dummy_driver import DummyWebDriver
from utils.comment import post_comment

comments = ["nice", "cool", "ban", "hello"]

CASES = []
for i in range(1, 351):
    CASES.append({
        "tc_id": f"TC_COMMENT_{i:04}",
        "name": f"test_comment_{i:04}",
        "module": "module_comment",
        "file": "tests/module_comment/test_comment.py",
        "text": comments[i % len(comments)]
    })

@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_comment(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open comments section")
    drv = DummyWebDriver()

    recorder.step("Step 2: Post comment")
    post_comment(data["text"])
