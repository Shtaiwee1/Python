from django.shortcuts import render , redirect

from .models import Dojo , Ninja



def index(request):
    # request.session['firstname']=request.POST['first_name']  
    # request.session['lastname']=request.POST['last_name']  
    # request.session['emailaddress']=request.POST['email']  
    # request.session['ageage']=request.POST['age']  
    # first_ninjas=Ninja.objects.filter(id=1)
    # second_ninjas=Ninja.objects.filter(id=2)
    # third_ninjas=Ninja.objects.filter(id=3)
    context = {
    "all_the_dojos":Dojo.objects.all(),
    "all_the_ninjas":Ninja.objects.all(),
    }
    
    return render(request, "index.html",context)


def create(request):
    request.session['dojoname']=request.POST['the_name']  
    request.session['city_loc']=request.POST['city']  
    request.session['state_loc']=request.POST['state']
    Dojo.objects.create(name=request.session['dojoname'],
                        city=request.session['city_loc'],
                        state=request.session['state_loc'],)
    return redirect('/')
                        
                        
def addninja(request):
    request.session['ninjaname']=request.POST['firstname']  
    request.session['ninjaname']=request.POST['firstname']  
    request.session['ninjalast']=request.POST['lastname']  
    request.session['dojo']=request.POST['dojo']  
    this_dojo = Dojo.objects.get(name = request.session['dojo'])

    Ninja.objects.create(first_name=request.session['ninjaname'],
                        last_name=request.session['ninjalast'],
                        dojo=this_dojo)
    return redirect('/')

def destroy(request):
    context = {
    "all_the_dojos":Dojo.objects.all(),
    "all_the_ninjas":Ninja.objects.all()
    }
    
    request.session['dojoname']=request.POST.get('delete')
    x=Dojo.objects.filter(name = request.session['dojoname'])
    x.delete()
    
    return redirect('/')
        
    
    





    