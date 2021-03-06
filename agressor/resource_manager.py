import os

from agressor.abc import ResourceManager
from agressor.state import is_lock, is_ready


class DataPackageResourceManager(ResourceManager):

    def __init__(self):
        self.folders = []

    def initialize(self, config):
        self._data_key = config["data_key"]

    @property
    def DATA_KEY(self):
        return self._data_key

    def register(self, folder):
        assert (os.path.exists(folder))
        self.folders.append(folder)

    def provide(self):
        for f in self.folders:
            if not is_lock(f) and is_ready(f):
                yield os.path.abspath(f)