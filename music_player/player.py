
import pygame
from pathlib import Path


class MusicPlayer:

    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = Path(music_folder)

        # Find all WAV and MP3 files
        self.playlist = sorted(
            list(self.music_folder.glob("*.wav")) +
            list(self.music_folder.glob("*.mp3"))
        )

        if not self.playlist:
            raise FileNotFoundError(
                "No music files found!"
            )

        self.current_track = 0
        self.is_playing = False
        self.durations = []

        # Load track durations
        for track in self.playlist:
            try:
                sound = pygame.mixer.Sound(str(track))
                self.durations.append(sound.get_length())
            except pygame.error:
                self.durations.append(0)

    def play(self):
        track = self.playlist[self.current_track]

        pygame.mixer.music.load(str(track))
        pygame.mixer.music.play()

        self.is_playing = True
        print("Playing:", track.name)

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current_track = (
            self.current_track + 1
        ) % len(self.playlist)
        self.play()

    def previous_track(self):
        self.current_track = (
            self.current_track - 1
        ) % len(self.playlist)
        self.play()

    def get_track_name(self):
        return self.playlist[self.current_track].name

    def get_position(self):
        position = pygame.mixer.music.get_pos()

        if position < 0:
            return 0

        return position // 1000

    def get_duration(self):
        return self.durations[self.current_track]

    def quit(self):
        pygame.mixer.music.stop()
        pygame.mixer.quit()

