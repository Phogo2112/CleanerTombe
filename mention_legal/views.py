from django.shortcuts import render

# Create your views here.
def mention_legal(request):
    return render(request, 'mention_legal/index.html')