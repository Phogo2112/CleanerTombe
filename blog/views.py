from django.shortcuts import render
from blog.data import get_tombe_list
# Create your views here.



def article(request,numero_article):
    
    return render(request, f"blog/article_{numero_article}.html")

# le ID mis dans les dictionnaire de la liste sert a donner un nom pour chaque grp ce qui erend chaque chose perso

def blog(request):
    tombe = get_tombe_list()
    return render(request, 'blog/index.html', {'tombe': tombe})

