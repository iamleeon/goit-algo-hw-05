from pathlib import Path
from collections import Counter
import sys

logs_file_path = str(Path(sys.argv[1]))


def choose_level():
    """defines if the script is launched with an additional argument"""
    level = "no_level"
    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
    elif len(sys.argv) > 3:
        level = sys.argv[2].upper()
        print("Only the second argument is taken.")
    return level


def parse_log_line(line: str) -> dict:
    """parses a log file and splits it into categories"""
    try:
        log_values = line.split()
        line_dict = {"data": log_values[0], "time": log_values[1], "level": log_values[2],
                     "message": " ".join(log_values[3:])}
        return line_dict
    except Exception as e:
        print(f"Parsing a log file failed. Error: {e}")
        # return None


def load_logs(file_path: str) -> list:
    """reads a log file and applies the parse_log_line func to it"""
    try:
        with open(file_path, "r", encoding="UTF-8") as log_file:
            logs_list = []
            for line in log_file:
                logs_list.append(parse_log_line(line))
            return logs_list
    except Exception as e:
        print(f"Loading logs failed. Error: {e}")
        # return None


def filter_logs_by_level(logs: list, level: str) -> list:
    """filters logs by level"""
    try:
        filtered_logs = list(filter(lambda log: log["level"] == level, logs))
        return filtered_logs
    except Exception as e:
        print(f"Filtering logs by level failed. Error: {e}")
        # return None


def count_logs_by_level(logs: list) -> dict:
    """counts logs be level"""
    try:
        levels_count_dict = dict(Counter(log["level"] for log in logs))
        return levels_count_dict
    except Exception as e:
        print(f"Counting logs by level failed. Error: {e}")
        # return None


def display_log_counts(counts: dict):
    """prints the results of logging level entries"""
    header = f"{"Logging level":<15} | {"Entries":<15}"
    divider = f"{"-" * 15} | {"-" * 15}"
    error_title = f"{"ERROR":<15} | {counts["ERROR"]:<15}"
    warning_title = f"{"WARNING":<15} | {counts["WARNING"]:<15}"
    info_title = f"{"INFO":<15} | {counts["INFO"]:<15}"
    debug_title = f"{"DEBUG":<15} | {counts["DEBUG"]:<15}"
    print(header, divider, error_title, warning_title, info_title, debug_title + "\n", sep="\n")
    level = choose_level()
    if level == "no_level":
        print("")
    elif level in counts:
        print(f"Log details for the {level} level:")
        logs = load_logs(logs_file_path)
        for line in logs:
            if level in line.values():
                print(" ".join(line.values()))
    else:
        print(f"No such level: {level}")


if __name__ == '__main__':
    choose_level()
    load_logs(logs_file_path)
    display_log_counts(count_logs_by_level(load_logs(logs_file_path)))
    filter_logs_by_level(load_logs(logs_file_path), choose_level())
    count_logs_by_level(load_logs(logs_file_path))
