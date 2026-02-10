import pytest
from utils.logger import PASS_LOG, FAIL_LOG


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    PASS_LOG.write_text("", encoding="utf-8")
    FAIL_LOG.write_text("", encoding="utf-8")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    recorder = getattr(item, "test_recorder", None)
    if report.when == "call" and recorder:
        if report.failed:
            exc = call.excinfo.value
            recorder.log_fail(exc)
        else:
            recorder.log_pass()
