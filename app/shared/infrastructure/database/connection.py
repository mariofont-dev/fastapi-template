from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    @abstractmethod
    def get_session(self):
        pass
