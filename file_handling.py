def log_activity(message):
    with open("activity_log.txt", "a") as file:
        file.write(f"{message}\n")