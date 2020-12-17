from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegisteration
from .models import User
# Create your views here.

# this function will add and show items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegisteration()
    else:
        fm = StudentRegisteration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})

#  this function update and Edit

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegisteration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegisteration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})




# this function will Delete

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
