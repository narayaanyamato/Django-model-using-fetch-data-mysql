from django.shortcuts import render
from modelapp2.models import Fruits
def show(request):
    data=Fruits.objects.all()
    f_rec={"data":data}
    return render(request,'Pages/fruits.html',f_rec)
