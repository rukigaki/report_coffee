import argparse

from factory import ReportExecutor
from reports import Report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", nargs="+")
    parser.add_argument("--report")
    args = parser.parse_args()

    report = ReportExecutor(base_cls=Report)
    report.execute(args.file, args.report)


if __name__ == "__main__":
    main()
