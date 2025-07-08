import status
import username
import logging

LOG_FILE = "login_system.log"

logger = logging.getLogger("log_event")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    # console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(LOG_FILE, mode="a")

    # console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # console_handler.setLevel(logging.INFO)
    # file_handler.setLevel(logging.DEBUG)

    # console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(formatter)

    # logger.addHandler(console_handler)
    logger.addHandler(file_handler)


    def log_event(username: str, status: str):
        log_message = f"Login event - Username: {username}, Status: {status}"
        if status == "success":
            logger.info(log_message)
        elif status == "expired":
            logger.warning(log_message)
        else:
            logger.error(log_message)

# Ручний запуск для перевірки
if __name__ == "__main__":
    log_event("alice", "success")
    log_event("Bob", "expired")
    log_event("carol", "failed")
    log_event("dave", "invalid")
    log_event("admin", "unknown")
    print(f"Логи записано у файл: {LOG_FILE}")


