from django.shortcuts import render

def error404(request, exception):
    return render(request, '404.html')

def error500(request, exception):
    return render(request, '500.html')