from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def under_construction(request):
    return render(request, 'underconstruction.html')