import pandas as pd
from datetime import datetime
from config import DOWNLOAD_DIR, FILE_PATH


def parse_excel(current_day) -> dict[str, str]:
    """Parses the Excel file from the diyanet website using pandas."""

    df = pd.read_excel(FILE_PATH, header=None, engine="openpyxl")

    # fix the column names
    df.columns = df.iloc[2]
    df = df[3:]
    df = df.reset_index(drop=True)

    # make the date column a date type
    df["Gregorianischen Kalender"] = pd.to_datetime(
        df["Gregorianischen Kalender"], dayfirst=True
    )  # dayfirst=True because format is DD.MM.YYYY

    row = df[df["Gregorianischen Kalender"].dt.date == current_day]

    prayer_times = {
        "Morgengebet": row["Morgengebet (Fastenbeginn )"].values[0],
        "Sonnenaufgang": row["Sonnenaufgang"].values[0],
        "Mittagsgebet": row["Mittagsgebet"].values[0],
        "Nachmittagsgebet": row["Nachmittagsgebet"].values[0],
        "Abendgebet": row["Abendgebet"].values[0],
        "Nachtgebet": row["Nachtgebet"].values[0],
    }

    return prayer_times
