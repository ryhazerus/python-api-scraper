log_line: int = 0


def pretty_log(msg: str):
    global log_line
    print(f"[INFO: Line {log_line}]:\t{msg}")
    log_line += 1
