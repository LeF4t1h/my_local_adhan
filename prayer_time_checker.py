from datetime import datetime


def check_prayer_time(prayer_times) -> bool:
    """Returns true if prayer time is valid."""
    if not prayer_times:
        return False

    times_to_check = [
        # prayer_times["Morgengebet"],
        prayer_times["Mittagsgebet"],
        prayer_times["Nachmittagsgebet"],
        prayer_times["Abendgebet"],
        prayer_times["Nachtgebet"],
    ]

    now = datetime.now().strftime("%H:%M")

    return now in times_to_check
