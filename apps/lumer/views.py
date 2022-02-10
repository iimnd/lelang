from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User


from django.shortcuts import render, redirect  
from apps.lumer.form import ItemForm  
from apps.lumer.models import Item



from datetime import date
import calendar
from calendar import HTMLCalendar


def emp(request):  
    if request.method == "POST":  
        form = ItemForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ItemForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Item.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Item.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Item.objects.get(id=id)  
    form = ItemForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Item.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  



def homePageView(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "asfasf - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    # user = User.objects.get(email="iim@alterra.id")
    # permissions = Permission.objects.filter(user)
    # # user = Permission.objects.get_user_permissions(email="iim@alterr.id")
    # return HttpResponse(permissions)

    return render(request, 'base2.html', {'title': title, 'cal': cal})


def homePageView2(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "asfasf - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    # user = User.objects.get(email="iim@alterra.id")
    # permissions = Permission.objects.filter(user)
    # # user = Permission.objects.get_user_permissions(email="iim@alterr.id")
    # return HttpResponse(permissions)

    return render(request, 'base2.html', {'title': title, 'cal': cal})
