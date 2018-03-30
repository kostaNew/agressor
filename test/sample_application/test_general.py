import unittest
import os

from agressor.main_manager import MainManager
from agressor.resource_manager import DataPackageResourceManager
from test.sample_application.step1.agressor import Agressor


class MyTestCase(unittest.TestCase):

    def test_DataPackageResourceManager(self):

        dprm = DataPackageResourceManager()
        dprm.initialize({"data_key": "TEST_DATA"})
        dprm.register('../data/pipeline1/case1')

        lst_ = list(dprm.provide())

        self.assertTrue(len(lst_) == 1)
        self.assertEquals('../data/pipeline1/case1', os.path.relpath(lst_[0]))

    def test_Agressor(self):
        agro = Agressor()
        agro.initialize({"folder_in": '../data/pipeline1/case1/'+agro.FOLDER_DATA_IN,
                         "folder_out": '../data/pipeline1/case1/'+agro.FOLDER_DATA})
        agro.look()
        agro.validate()

    def test_MainManager(self):
        agro = Agressor()
        dprm = DataPackageResourceManager()
        dprm.initialize({"data_key": "TEST_DATA"})
        dprm.register('../data/pipeline1/case1')

        main_manager = MainManager()
        main_manager.register_agressor(agro)
        main_manager.register_resource_manager(dprm)
        main_manager.process_once()

if __name__ == '__main__':
    unittest.main()
