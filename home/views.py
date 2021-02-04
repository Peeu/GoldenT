from datetime import datetime

from django.shortcuts import render

from home.models import Contact


# Create your views here.
def index(request):
    context = {
        "variable1": "Variable1 value",
        "variable2": "Variable2 value"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")


def store(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact1 = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact1.save()
    return render(request, 'contact.html')
