import pytest
from utils.recorder import TestRecorder
from utils.dummy_driver import DummyWebDriver
from utils.search import search

queries = ["music", "timeout", "empty", "live"]

CASES = []
for i in range(1, 351):
    CASES.append({
        "tc_id": f"TC_SEARCH_{i:04}",
        "name": f"test_search_{i:04}",
        "module": "module_search",
        "file": "tests/module_search/test_search.py",
        "query": queries[i % len(queries)]
    })

@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_search(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open search page")
    drv = DummyWebDriver()

    recorder.step("Step 2: Perform search")
    search(data["query"])
