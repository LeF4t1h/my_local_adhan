import time
import vlc
from config import AUDIO_FILE_PATH


def play_adhan():
    """Plays the adhan mp3 file when now == prayer time"""

    player = vlc.MediaPlayer(AUDIO_FILE_PATH)
    player.play()
    time.sleep(1)  # small delay before checking if playback has started
    while player.is_playing():
        time.sleep(0.1)
    player.stop()
