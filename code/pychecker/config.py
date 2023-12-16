import os


ROOT = os.path.dirname(__file__)
CACHE_DIR = os.path.join(ROOT, "cache")
LOG_DIR = os.path.join(ROOT, "log")
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

LOG_FORMAT = "%(asctime)s [%(levelname)s]  %(message)s"


PY_VERSIONS = ["2.7", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10"]


