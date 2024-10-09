from django.db import models

class SongSuggestion(models.Model):
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    suggested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.song_name} by {self.artist_name}"
