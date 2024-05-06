from pathlib import Path
import sys


logs_file_path = Path(sys.argv[1])


# defines if the script is launched with an additional argument
def choose_level():
    if len(sys.argv) == 3:
        level = sys.argv[2].lower()
    elif len(sys.argv) > 3:
        level = sys.argv[2].lower()
        print("Only the second argument is taken.")
    else:
        level = None
    return level


# parses a log file, splits it into categories and creates a dict
def parse_log_line(line: str) -> dict:
    log_values = line.split()
    line_dict = {"data": log_values[0], "time": log_values[1], "level": log_values[2],
                 "message": " ".join(log_values[3:])}
    return line_dict


# reads a log file and applies the parse_log_line func to it. Throws errors if the file doesn't exist or can't be read
def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="UTF-8") as log_file:
            logs_list = []
            for line in log_file:
                logs_list.append(parse_log_line(line))
            return logs_list
    except FileNotFoundError:
        print(f"FileNotFoundError: No such file or directory: {file_path}")
    except UnicodeDecodeError:
        print(f"UnicodeDecodeError: 'utf-8' codec can't decode {file_path}")


# if a level is in logs, prints lines with level
def filter_logs_by_level(logs: list, level: str) -> list:
    if level is None:
        print('')
    elif level.upper() in count_logs_by_level(logs_file_path):
        print(f"Log details for the {level.upper()} level:")
        logs = load_logs(logs_file_path)
        for line in logs:
            if level.upper() in line.values():
                print(" ".join(line.values()))
    else:
        print(f"No such level: {level}")


# counts logs be level and returns a dict
def count_logs_by_level(logs: list) -> dict:
    logs = load_logs(logs_file_path)
    levels_dict = {"ERROR": 0, "WARNING": 0, "INFO": 0, "DEBUG": 0}
    try:
        for line in logs:
            if "ERROR" in line.values():
                levels_dict["ERROR"] += 1
            elif "WARNING" in line.values():
                levels_dict["WARNING"] += 1
            elif "INFO" in line.values():
                levels_dict["INFO"] += 1
            elif "DEBUG" in line.values():
                levels_dict["DEBUG"] += 1
        return levels_dict
    except TypeError:
        return levels_dict


# prints the results of logging level entries
def display_log_counts(counts: dict):
    header = f"{"Logging level":<15} | {"Entries":<15}"
    divider = f"{"-" * 15} | {"-" * 15}"
    counts = count_logs_by_level(logs_file_path)
    error_title = f"{"ERROR":<15} | {counts["ERROR"]:<15}"
    warning_title = f"{"WARNING":<15} | {counts["WARNING"]:<15}"
    info_title = f"{"INFO":<15} | {counts["INFO"]:<15}"
    debug_title = f"{"DEBUG":<15} | {counts["DEBUG"]:<15}"
    print(header, divider, error_title, warning_title, info_title, debug_title + "\n", sep="\n")


if __name__ == '__main__':
    choose_level()
    load_logs(logs_file_path)
    display_log_counts(count_logs_by_level)
    filter_logs_by_level(logs_file_path, choose_level())
    count_logs_by_level(logs_file_path)
