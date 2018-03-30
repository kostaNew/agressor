import os

from agressor.abc import *

FILE_AGRO_READY = '.agro_ready'

class MainManager:

    def __init__(self):
        self._agressors = []
        self._resources = []

    def register_agressor(self, agressor):
        assert (issubclass(type(agressor), BaseAgressor))
        self._agressors.append(agressor)

    def register_resource_manager(self, res_manager):
        assert (issubclass(type(res_manager), ResourceManager))
        self._resources.append(res_manager)

    def process_once(self):
        for res in self._resources:
            for agro in self._agressors:
                if res.DATA_KEY==agro.DATA_KEY:
                    if issubclass(type(agro), DataPackageMixin):
                        for folder in res.provide():

                            folder_in = os.path.join(folder, agro.FOLDER_DATA_IN)
                            folder_out = os.path.join(folder, agro.FOLDER_DATA)

                            config = {}
                            config['folder_in'] = folder_in
                            config['folder_out'] = folder_out
                            agro.initialize(config)

                            if agro.look():
                                if agro.validate():
                                    agro.process()




