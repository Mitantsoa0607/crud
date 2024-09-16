from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserForm
from .models import User


def index(request):
    users=User.objects.all()
    return render(request, 'crud/index.html',{'users' : users})

def create(request):
    if request.method=='POST':
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=UserForm()
    return render(request,'crud/create.html',{'form': form})

def edit(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method=='POST':
        form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=UserForm(instance=user)
    return render(request,'crud/edit.html',{'form':form})

def delete(request,pk):
    user=get_object_or_404(User, pk=pk)
    if request.method=='POST':
        user.delete()
        return redirect('index')
    return render(request,redirect('index'),{'user':user})