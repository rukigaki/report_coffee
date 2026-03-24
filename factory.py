from tabulate import tabulate


class ReportExecutor:
    def __init__(self, base_cls):
        self.base_cls = base_cls

    def get_report(self, files, report_type):
        report_class = self.base_cls.registry.get(report_type)
        return report_class(files)

    def execute(self, files, report_type):
        report = self.get_report(files, report_type)
        report.load_data()
        prepare_data = report.transform_data()

        print(tabulate(tabular_data=prepare_data, headers=["student", report_type], tablefmt='fancy_grid'))
