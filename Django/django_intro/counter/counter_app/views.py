
from django.shortcuts import render , redirect 

def index(request):
    if not 'counter' in request.session:
        request.session['counter'] =0
    else:
        request.session['counter'] +=1

    if not 'visits' in request.session:
        request.session['visits'] =0
    else:
        request.session['visits'] +=1
    return render(request,'index.html')


def destroy(request):
    del request.session['counter']
    request.session['counter'] =0
    return redirect('/')

def add(request):  
    request.session['counter'] +=2
    return render(request,'index.html')


def choose(request,x): 
    request.session['counter'] +=int(x)
    return render(request,'index.html')

def increments(request):
    request.session['counter'] +=int(request.POST['reply'])
    return render(request,'index.html')
    
    
    # if 'message' in request.POST:
        # var=request.value.get('x')
        # context={'var':int(x)} 