from datetime import datetime
import re
import os

def analyze_heartbeat(log_file_path, output_file_path, target_key="Key TSTFEED0300|7E3E|0400"):
    pattern = re.compile(r"Timestamp (\d{2}:\d{2}:\d{2})")

    filtered_lines = []
    timestamps = []

    # 1. Читаємо файл та фільтруємо по ключу
    with open(log_file_path, "r") as f:
        for line in f:
            if target_key in line:
                match = pattern.search(line)
                if match:
                    time_obj = datetime.strptime(match.group(1), "%H:%M:%S")
                    timestamps.append(time_obj)

    # 2. Аналізуємо інтервали heartbeat
    log_entries = []

    for i in range(len(timestamps) - 1):
        delta = abs((timestamps[i] - timestamps[i + 1]).total_seconds())

        if 31 < delta < 33:
            log_entries.append(f"[{timestamps[i].strftime('%H:%M:%S')}] WARNING: Heartbeat interval = {int(delta)}s")
        elif delta >= 33:
            log_entries.append(f"[{timestamps[i].strftime('%H:%M:%S')}] ERROR: Heartbeat interval = {int(delta)}s")

    # 3. Запис результатів у файл
    with open(output_file_path, "w") as out_file:
        for entry in log_entries:
            out_file.write(entry + "\n")

    # 4. Повідомлення про успіх
    print(f"✅ Аналіз завершено. Результати записані у файл: {output_file_path}")
    print(f"📁 Повний шлях до файлу: {os.path.abspath(output_file_path)}")
    if not log_entries:
        print("ℹ️ Усі heartbeat інтервали в нормі (≤ 31 сек)")

# Запуск якщо скрипт запускається напряму
if __name__ == "__main__":
    analyze_heartbeat("hblog.txt", "hb_test.log")
