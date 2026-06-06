def process_file(filename):
    with open(filename, "r") as file:
        for line in file:
            if "CPU_SPIKE" in line:
                # 'yield' pauses the function and returns this single line.
                # The next time the function is called, it picks up exactly here.
                yield line


with open("test_logs.txt", "w") as f:
    f.write("INFO: OK\nCPU_SPIKE: 99%\nINFO: OK\nCPU_SPIKE: 100%\nINFO: OK\nCPU_NORMAL: 1%\n")

if __name__ == "__main__":
    for bad_log in process_file("test_logs.txt"):
        print("Found a spike:", bad_log.strip())