from django.shortcuts import render


def index(request):
    return render(request, "portfolio/pf_index.html")
