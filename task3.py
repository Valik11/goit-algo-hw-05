import re
import sys

def parse_log_line(line: str) -> dict:
    """Parse a log line and extract its components."""
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
    match = re.match(pattern, line)
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    else:
        return None

def load_logs(file_path: str) -> list:
    """Load logs from a file and parse them."""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_data = parse_log_line(line.strip())
                if log_data:
                    logs.append(log_data)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by the specified log level."""
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    """Count the number of logs for each log level."""
    log_counts = {}
    for log in logs:
        level = log['level']
        log_counts[level] = log_counts.get(level, 0) + 1
    return log_counts

def display_log_counts(counts: dict):
    """Display the log counts in a formatted table."""
    print("Log Level | Count")
    print("-----------------")
    for level, count in counts.items():
        print(f"{level.upper():<10} | {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path> [log_level]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = None
    if len(sys.argv) == 3:
        log_level = sys.argv[2]

    logs = load_logs(log_file_path)
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        display_log_counts(count_logs_by_level(filtered_logs))
        print(f"\nDetails of logs for level '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")
    else:
        display_log_counts(count_logs_by_level(logs))
