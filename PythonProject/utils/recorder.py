import traceback
from utils.logger import get_logger, PASS_LOG, FAIL_LOG


class TestRecorder:
    def __init__(self, tc_id, name, module, file_relpath):
        self.tc_id = tc_id
        self.name = name
        self.module = module
        self.file_relpath = file_relpath
        self.steps = []

    def step(self, text):
        self.steps.append(text)

    def log_pass(self):
        logger = get_logger("PASS", PASS_LOG)
        logger.info(
            f"""
TestCaseName: {self.name}
TestCaseID: {self.tc_id}
Module: {self.module}
Status: PASSED
FilePath: {self.file_relpath}
Steps:
""" + "\n".join(f"  - {s}" for s in self.steps)
        )

    def log_fail(self, exc):
        logger = get_logger("FAIL", FAIL_LOG)
        stacktrace = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))

        logger.error(
            f"""
TestCaseName: {self.name}
TestCaseID: {self.tc_id}
Module: {self.module}
Status: FAILED
ExceptionType: {type(exc).__name__}
FilePath: {self.file_relpath}
Steps:
StackTrace:
{stacktrace}
""" + "\n".join(f"  - {s}" for s in self.steps)
        )
