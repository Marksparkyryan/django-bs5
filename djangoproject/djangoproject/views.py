from django.shortcuts import render


def cheatsheet(request):
    return render(request, 'cheatsheet.html')
    