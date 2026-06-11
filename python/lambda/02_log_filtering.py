logs = ["INFO: Server up", "ERROR: DB Timeout", "WARN: CPU High", "ERROR: Out of Memory"]

error_logs = list(filter(lambda str: "ERROR" in str, logs))
print(error_logs)