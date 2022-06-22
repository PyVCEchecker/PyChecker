import os
import logging
from datetime import datetime
from tqdm import tqdm

import pychecker.config as config
from pychecker.utils import read_object_from_file, write_object_to_file
from pychecker.check.no_avl_resource_detection import parse_comp_expr
from pychecker.check.visit_pypi import get_metadata
from pychecker.check.check import check_pkgver
from pychecker.check.experiment.exp_config import IN_THE_FIELD_ROOT


now = datetime.now()
log_name = "Detection.{}{:02d}{:02d}.log".format(now.year, now.month, now.day)
logging.basicConfig(filename=os.path.join(config.LOG_DIR, log_name),
                    level=logging.INFO, format=config.LOG_FORMAT)


class Detection:
    def __init__(self, projects=500):
        self.root = IN_THE_FIELD_ROOT
        self.data = self.read_data(projects)

    def read_data(self, projects=500):
        data_path = os.path.join(self.root, "data.json")
        data = read_object_from_file(data_path)
        if not data or len(data) < projects:
            data = self.prepare_data(data_path, projects)
        return data

    def prepare_data(self, path, projects):
        data = dict()  # key: pkg#ver, val: comp_expr
        pkg_dict = read_object_from_file(os.path.join(self.root, "packages_10000.json"))
        pkgver_dict = read_object_from_file(os.path.join(self.root, "package_versions.json"))
        pkgs = list(pkg_dict.keys())[3010:]  # pkgs in the field
        count = 0
        for pkg in tqdm(pkgs):
            try:
                latest = list(pkgver_dict[pkg].keys())[-1]
            except (KeyError, IndexError):
                continue
            metadata = get_metadata(pkg, latest)
            if not metadata:
                continue
            comp_expr = metadata["requires_python"]
            key = f"{pkg}#{latest}"
            data[key] = comp_expr
            count += 1
            if count >= projects:
                break
        write_object_to_file(path, data)
        return data

    def detect(self, start=None, end=None):
        if not start:
            start = 0
        if not end:
            end = len(self.data.items())
        detected_count = 0
        for key, value in tqdm(list(self.data.items())[start:end]):
            pkg, ver = key.split("#")
            pyvers = set(parse_comp_expr(value, config.PY_VERSIONS))
            result = check_pkgver(pkg, ver, cache_path=self.root, save_files=True)
            if True not in result:
                continue
            # print(key, result)
            logging.log(logging.INFO, f"{pkg}-{ver}, {int(result[0])}, {int(result[1])}, {int(result[2])}")
            detected_count += 1
        print(f"{detected_count} errors detected.")


if __name__ == '__main__':
    detection = Detection(1000)
    detection.detect(500)
