"""
Ввиду того, что проект маленький, я добавил для наглядности два класса для того,
чтобы показать, что проект может легко масштабироваться. По-хорошему, их также стоит разнести по разным модулям, но из-за
того, что в данном случае они представлены больше, как заглушки, нежели реально боевыми классами, я решил их оставить здесь.

"""

import statistics

from .base import Report


@Report.register("median-coffee")
class MedianCoffee(Report):
    def transform_data(self):
        data = {row["student"]: [] for row in self.raw_data}  # Тернарный оператор создает разные ссылки на []
        for row in self.raw_data:
            data[row["student"]].append(int(row["coffee_spent"]))

        median_data = zip(data, map(statistics.median, data.values()))
        sorted_data = sorted(median_data, key=lambda x: x[1], reverse=True)

        return sorted_data


@Report.register("another-report")
class AnotherReport(Report):
    def transform_data(self):
        ...


@Report.register("additional-report")
class AdditionalReport(Report):
    def transform_data(self):
        ...
