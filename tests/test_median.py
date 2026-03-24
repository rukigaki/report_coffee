from reports.median_coffee import MedianCoffee
from reports import Report
from factory import ReportExecutor


def test_transform_data():
    report = MedianCoffee(files=[])

    report.raw_data = [
        {"student": "Vlad", "coffee_spent": 2},
        {"student": "Vlad", "coffee_spent": 4},
        {"student": "Alex", "coffee_spent": 3},
    ]

    result = report.transform_data()

    assert result == [
        ("Vlad", 3),
        ("Alex", 3),
    ]

def test_transform_data_empty():
    report = MedianCoffee(files=[])

    result = report.transform_data()

    assert result == []

def test_report_registry_contains_median():
    assert "median-coffee" in Report.registry


def test_report_registry_points_to_correct_class():
    assert Report.registry["median-coffee"] is MedianCoffee


def test_executor_get_report():
    executor = ReportExecutor(base_cls=Report)

    report = executor.get_report(files=[], report_type="median-coffee")

    assert isinstance(report, MedianCoffee)
