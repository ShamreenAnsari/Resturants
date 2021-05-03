from django.shortcuts import render,HttpResponse
from django.template import loader
from menu.models import menu
# Create your views here.
# def index(request):
#     template=loader.get_template('index.html')
#     return HttpResponse(template.render())

# def about_us(request):
#     template=loader.get_template('about_us.html')
#     return HttpResponse(template.render())

# def menus(request):
#     template=loader.get_template('menus.html')
#     return HttpResponse(template.render())

from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'name':'ram',
        'message':'this is simple message'
    }
    return render(request,'index.html',context)


def menus(request):
    if request.method =="POST":
        number=request.POST.get('number')
        name=request.POST.get('name')
        price=request.POST.get('price')
        menus=menu(number=number,name=name,price=price)
        menus.save()
    return render(request,'menus.html')


def about_us(request):
    return render(request,'about_us.html')

# def login(request):
#     return render(request,"/admin")

# def upload(request):
#     return render(request,'upload.html')







