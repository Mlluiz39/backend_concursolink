from abc import ABC, abstractmethod
import time
import random

class BaseScraper(ABC):

    def __init__(self, delay_range=(1,3)):
        self.delay_range = delay_range

    def delay(self):
        time.sleep(random.uniform(*self.delay_range))

    @abstractmethod
    def buscar_vagas(self):
        pass