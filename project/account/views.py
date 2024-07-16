from django.shortcuts import redirect, render
from .models import *
from .forms import *


def register(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = UserForm()
  return render(request,'account/register.html',{'form':form})

def home(request):
    return render(request, 'account/home.html')


