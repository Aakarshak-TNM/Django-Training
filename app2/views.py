from django.shortcuts import render

# Create your views here.


def navbar(request):
    # return HttpResponse("Hello World")
    return render(request, "app/navbar.html")


def contact(request):
    # return HttpResponse("Hello World")
    return render(request, "app/contact.html")
