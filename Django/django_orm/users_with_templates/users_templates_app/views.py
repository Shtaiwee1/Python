from django.shortcuts import render , redirect 
from .models import User



def index(request):
    context = {
    "all_the_users": User.objects.all()
    }
    return render(request, "index.html", context)


def add(request):
    request.session['firstname']=request.POST['first_name']  
    request.session['lastname']=request.POST['last_name']  
    request.session['emailaddress']=request.POST['email']  
    request.session['ageage']=request.POST['age']  
    User.objects.create(first_name=request.session['firstname'],
                        last_name=request.session['lastname'],
                        email_address=request.session['emailaddress'],
                        age=request.session['ageage'])
    context={
    "all_the_users":User.objects.all()}
    return render(request, "index.html",context)

def destroy(request):
    delete_users= User.objects.all()
    delete_users.delete()
    # del request.session['firstname']
    # del request.session['lastname']
    # del request.session['emailaddress']
    # del request.session['ageage']
    return redirect('/')

