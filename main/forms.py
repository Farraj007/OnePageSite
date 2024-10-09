# forms.py
from django import forms

class SongSuggestionForm(forms.Form):
    song_name = forms.CharField(max_length=100, label="Song Name")
    artist_name = forms.CharField(max_length=100, label="Artist Name")
