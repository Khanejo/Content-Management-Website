from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm ,goodsForm
from django.http import Http404
from datetime import  datetime,timedelta,date
from collections import defaultdict
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import goods
from .tables import SimpleTable
from django.http import HttpResponse, HttpResponseRedirect
from django_tables2 import RequestConfig

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def goods_smuggle(request):
    form = None
    good_name =None
    expiry_date =None
    endrr=None
    e=None
    d=None
    usee=None
    useful_obj =None
    if request.method == 'POST' or None:       
        form = goodsForm(request.POST or None)
        if form.is_valid():
            
            equipment_name = form.cleaned_data.get("equipment_name")
            information = form.cleaned_data.get("information")
            is_obj_under_amc = form.cleaned_data.get("is_obj_under_amc")
            software_ver =form.cleaned_data.get("software_ver")
            quantity = form.cleaned_data.get("quantity")
            begin_date = form.cleaned_data.get("begin_date")
            expirry_date = form.cleaned_data.get("expiry_date")
            serial_no=  form.cleaned_data.get("serial_no")
            form.save()
            return HttpResponseRedirect('/home/')

    return render(request,"goods.html",{'form':form , 'good_name':usee,'endrr':endrr,})


def homepage(request):
    usee =None
    useful_obj= None
    den= None
    form = None
    resultant=None
    listt = None
    tusi = None
    resultant= None

    futuredate = date.today() + timedelta(days= 30)
    e = goods.objects.values_list('expiry_date')
    listt= goods.objects.values_list('equipment_name').distinct()
    f = goods.objects.order_by('expiry_date')
    g = goods.objects.filter(expiry_date__range =[date.today(),futuredate] )
    tusi = g.values("equipment_name","expiry_date","serial_no")
    table = SimpleTable(tusi)
    RequestConfig(request).configure(table)

    selected = request.POST.get('item_id')
    try:
        ll =eval(selected)[0]
        resultant=goods.objects.filter(equipment_name=ll).values()

    except TypeError or AttributeError:
        pass

    
    
     



   
        
            

    return render(request, "home.html",{ 'good_name':tusi,'m':listt,'gut':listt[0],'s':resultant})


