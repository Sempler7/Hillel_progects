import subprocess
import time
import requests
import signal
import os
import sys

FLASK_SCRIPT = "cars_app.py"
BASE_URL = "http://127.0.0.1:8080/cars"

def wait_for_server(timeout=15):
    for i in range(timeout):
        try:
            response = requests.get(BASE_URL)
            if response.status_code in [200, 401]:
                print("✅ Flask-сервер готовий")
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    print("❌ Сервер не відповідає")
    return False

def main():
    print("🚀 Запускаємо Flask-сервер...")
    flask_proc = subprocess.Popen(
        [sys.executable, FLASK_SCRIPT],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
    )

    if not wait_for_server():
        flask_proc.terminate()
        sys.exit(1)

    print("🧪 Запускаємо pytest...")
    result = subprocess.run(["pytest", "test_cars_api.py"])

    print("🛑 Завершуємо Flask-сервер...")
    if os.name == "nt":
        flask_proc.send_signal(signal.CTRL_BREAK_EVENT)
    else:
        flask_proc.terminate()

    sys.exit(result.returncode)

if __name__ == "__main__":
    main()