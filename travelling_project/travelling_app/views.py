from django.shortcuts import render

from travelling_app.models import Places


# Create your views here.
def fun(request):
    obj=Places.objects.all
    return render(request,'index.html',{'result':obj})
