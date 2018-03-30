import os
from abc import ABCMeta, abstractmethod

class ResourceManager:
    """This class describe resource for agressors: folders with experiments, clusters, free time"""
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def DATA_KEY(self):
        pass

    @abstractmethod
    def initialize(self, config):
        pass

    @abstractmethod
    def register(self, folder):
        """
        Register a resource
        :param folder: In the
        :return:
        """
        pass

    @abstractmethod
    def provide(self):
        pass

class BaseAgressor:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def DATA_KEY(self):
        pass

    @abstractmethod
    def initialize(self, config):
        pass

    @abstractmethod
    def look(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def process(self):
        pass

class DataPackageMixin:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def FOLDER_DATA_IN(self):
        pass

    @property
    @abstractmethod
    def FOLDER_DATA(self):
        pass

class BaseTask:
    __metaclass__ = ABCMeta

    @abstractmethod
    def detect_state(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def terminate(self):
        pass