from django.shortcuts import render
from django.http import HttpResponse

def food(request):
    return render(request=request, template_name='index.html', context={})
