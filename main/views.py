# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SongSuggestionForm

def index(request):
    form = SongSuggestionForm()

    if request.method == 'POST':
        form = SongSuggestionForm(request.POST)
        if form.is_valid():
            # Get the form data
            song_name = form.cleaned_data['song_name']
            artist_name = form.cleaned_data['artist_name']

            # You can store the data, send an email, etc.
            # For now, we'll just display a success message
            messages.success(request, f"Suggested: {song_name} by {artist_name}")

            return redirect('index')

    return render(request, 'index.html', {'form': form})

def under_construction(request):
    return render(request, 'underconstruction.html')
