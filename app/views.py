from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from .models import Task
from .forms import TaskForm,RegUser
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def index(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'index.html',{'tasks':tasks})
@login_required(login_url='login')
def add(request):
    if request.method=='POST':
        ordinary_dict = {'user':request.user}
        query_dict = QueryDict('', mutable=True)
        query_dict.update(ordinary_dict)
        query_dict.update(request.POST)
        form=TaskForm(query_dict)
        if form.is_valid():
            form.save()
            return redirect('index')
    form=TaskForm()
    return render(request,'add.html',{'form':form})
@login_required(login_url='login')
def update(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
        ordinary_dict = {'user':request.user}
        query_dict = QueryDict('', mutable=True)
        query_dict.update(ordinary_dict)
        query_dict.update(request.POST)
        form=TaskForm(query_dict,instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    form=TaskForm(instance=task)
    return render(request,'update.html',{'form':form})
@login_required(login_url='login')
def delete(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=="POST":
        task.delete()
        return redirect('index')
    return render(request,'del.html',{'task':task})

def reg(request):
    if request.method=='POST':
        form=RegUser(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            user=authenticate(request,
            username=request.POST['username'],
            password=request.POST['password1']
            )
            login(request,user)
            return redirect('index')
        else:
            messages.warning(request,'Invalid form, Please try again!')
            return render(request,'reg.html',{'form':form})
    form=RegUser()
    return render(request,'reg.html',{'form':form})
def loginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
        return redirect('index')
    form=RegUser()
    return render(request,'login.html',{'form':form})
def logouter(request):
    logout(request)
    return redirect('login')