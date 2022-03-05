from abc import ABC, abstractmethod


class Attacker(ABC):
    @abstractmethod
    def run(self):
        ...
