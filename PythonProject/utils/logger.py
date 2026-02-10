import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

PASS_LOG = LOG_DIR / "pass.log"
FAIL_LOG = LOG_DIR / "fail.log"


def get_logger(name, logfile):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Always recreate handler to avoid dead handlers after cleanup
    if logger.handlers:
        for h in list(logger.handlers):
            logger.removeHandler(h)
            h.close()

    handler = logging.FileHandler(logfile, mode="a", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
