import csv
from abc import ABC, abstractmethod


class Report(ABC):
    registry = {}

    def __init__(self, files):
        self.files = files
        self.raw_data = []

    @classmethod
    def register(cls, name):
        def decorator(subclass):
            cls.registry[name] = subclass
            return subclass

        return decorator

    def load_data(self):
        for file in self.files:
            with open(file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.raw_data.extend(reader)

    @abstractmethod
    def transform_data(self):
        pass