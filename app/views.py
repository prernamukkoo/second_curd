from django.shortcuts import render, redirect
from . forms import StudentRegisteation
from . models import User

# Create your views here.
# this function wil add new items abd show data.
def add(request):
    temp='enroll/add.html'
    if request.method=='POST':
       fm= StudentRegisteation(request.POST)
       if fm.is_valid():
        nm = fm.cleaned_data['name']
        em = fm.cleaned_data['email']
        pwd = fm.cleaned_data['password']
        reg = User(name=nm,email=em,password=pwd)
        reg.save()
        fm=StudentRegisteation()
        # fm.save()
    else:
        fm=StudentRegisteation()
    stub = User.objects.all()   
    return render(request,temp,{'form':fm,'stu':stub})
#this function is delete data.
# def delete_data(request):
#     if request.method =='POST':
#         pi =User.objects.get(__package__=id)
#         pi.delete()
#         return HttpResponseRedirect('/')
def delete_data(request, id):
  member = User.objects.get(id=id)
  member.delete()
  return redirect('add')    

# this function will update and edit data.

def update_data(request,id):
    temp= 'enroll/update.html'
    if request.method =='POST':
        pi= User.objects.get(id=id)
        fm=StudentRegisteation(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else: 
        pi= User.objects.get(id=id)
        fm=StudentRegisteation(instance=pi)   
    return render(request,temp,{'form':fm})

# def update_data(request,id):
#     template = 'enroll/update.html'
#     data1 = User.objects.get(id=id)
#     context ={
#         'form': StudentRegisteation(instance=data1)
#     }
#     if request.method == 'POST':
#         form = StudentRegisteation(instance=data1, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add')
#     return render(request, template, context)


