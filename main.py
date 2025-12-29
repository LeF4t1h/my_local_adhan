from datetime import datetime
import time
import os

from audio_player import play_adhan
from config import DOWNLOAD_DIR, FILE_PATH
from excel_downloader import download_excel
from prayer_time_parser import parse_excel
from prayer_time_checker import check_prayer_time

# keep track of last year and last day
last_year = datetime.now().year
last_day = datetime.now().date()

# --- Initial setup: ensure prayer_times available immediately ---
# Download Excel if not present (or optionally always download)
print("Downloading Excel file...")
download_excel() if not os.path.exists(FILE_PATH) else None
prayer_times = parse_excel(last_day)
print(f"Prayer times for {last_day}:")
print(prayer_times)

def main():
    global last_year, last_day, prayer_times

    while True:
        now = datetime.now()
        current_year = now.year
        current_day = now.date()

        # --- New year check ---
        if current_year != last_year:
            print(f"🎉 Happy New Year! New year detected: {current_year}")

            # delete old downloads
            for filename in os.listdir(DOWNLOAD_DIR):
                file_path = os.path.join(DOWNLOAD_DIR, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("All files deleted from", DOWNLOAD_DIR)

            # download new Excel file
            print("Downloading Excel file...")
            download_excel()
            last_year = current_year

        # --- New day check ---
        if current_day != last_day:
            print(f"🌞 New day detected: {current_day}")

            # parse the Excel for today's prayer times
            prayer_times = parse_excel(current_day)
            print(f"Prayer times for {current_day}:")
            print(prayer_times)

            last_day = current_day

        # --- Loop to check if prayer time has come ---
        if check_prayer_time(prayer_times):
            print("Playing adhan...")
            play_adhan()

        # wait 60 seconds before next check
        time.sleep(60)


if __name__ == "__main__":
    main()
