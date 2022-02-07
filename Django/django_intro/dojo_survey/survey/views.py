from django.shortcuts import render, HttpResponse , redirect


def index(request):
    return render(request,"index.html")



def users(request):
    context={
        'name_form':request.POST['name'],
        'location_form':request.POST['location'],
        'favourite_form':request.POST['favourite'],
        'comment_form':request.POST['comment'],
        'gender_form':request.POST['gender'],
        'check_form':request.POST.getlist('check')
    }
    return render(request,'result.html',context)


def home(request):
    return redirect("/")