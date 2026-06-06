mock_logs = [
    "INFO: Server started",
    "ERROR: Database connection failed",
    "WARN: CPU usage high",
    "ERROR: Timeout on endpoint /api/users"
]
def extract_errors(log_lines):
    error_lines = []
    for line in log_lines:
        if("ERROR" in line):
            error_lines.append(line)
    return error_lines
    # or 
    # return [line for line in log_lines if "ERROR" in line] - list comprehension is fast as it is written in c under the hood


def count_erros(error_list):
    return len(error_list)

if __name__ == "__main__":
    error_list = extract_errors(mock_logs)
    print("errors:", error_list)
    print(count_erros(error_list))
