from django.shortcuts import render,redirect
import random

def index(request):
    
    request.session['counter'] =0
    request.session['x']=random.randint(1, 100)
    return render(request,'index.html')

def destroy(request):
    request.session['counter'] =0
    del request.session['x']
    del request.session['y']
    return redirect('/')

def comparison(request):
    if not 'counter' in request.session:
        request.session['counter'] =0
    else:
        request.session['counter'] +=1
    request.session['y']=int(request.POST['guess'])
    print('*'*80)
    print(request.session['x'])
    return redirect('/goback')

def goback_function(request):
    return render(request,'index.html')

def winners(request):
    if request.POST['user'] not in request.session:
        request.session['z']= request.POST['user']
        
    request.session['attempts']=request.session['counter']
    request.session['z']= request.POST['user'] 
    return render(request,'winners.html')  






# Create your views here.
