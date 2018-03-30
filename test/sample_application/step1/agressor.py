import unittest
import numpy as np
import shutil

from agressor.abc import BaseAgressor, DataPackageMixin
from agressor.helpers import *

FILE_TXT = 'data.txt'

class Agressor(BaseAgressor, DataPackageMixin):

    @property
    def DATA_KEY(self):
        return "TEST_DATA"

    @property
    def FOLDER_DATA_IN(self):
        return "s100_original"

    @property
    def FOLDER_DATA(self):
        return "s200_statistics"

    def initialize(self, config):
        self.folder_in = config['folder_in']
        self.folder_out = config['folder_out']

    def look(self):
        return check_path_structure(self.folder_in, [FILE_TXT])

    def validate(self):
        np.loadtxt(os.path.join(self.folder_in, FILE_TXT))
        return True

    def process(self):
        os.makedirs(self.folder_out, exist_ok=True)
        shutil.copy(os.path.join(self.folder_in, FILE_TXT), os.path.join(self.folder_out, FILE_TXT))
        return True