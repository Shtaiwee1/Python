from django.shortcuts import render , redirect
import random

def index(request):
    return render(request,'index.html')


def process(request):
    farm = request.POST.get('farm')
    cave = request.POST.get('cave')
    house = request.POST.get('house')
    casino = request.POST.get('casino')
    request.session['total'] += request.session['gained'] 
    
    request.session['gained']=0
    if farm == 'farm':
        x = random.randint(10, 20)
        request.session['gained'] += x
        return redirect('/') 
    elif cave == 'cave':
        x = random.randint(5, 10)
        request.session['gained'] += x
        return redirect('/') 
    elif house == 'house':
        x = random.randint(2, 5)
        request.session['gained'] += x
        return redirect('/') 
    elif casino == 'casino':
        x = random.randint(0, 50)
        request.session['gained'] += x
        return redirect('/') 
    return redirect('/')


# def findplace(request , y):
#     farm = request.POST.get('farm')
#     cave = request.POST.get('cave')
#     house = request.POST.get('house')
#     casino = request.POST.get('casino')
#     request.session['total'] += request.session['gained'] 
    
#     request.session['gained']=0
#     if y == 'farm':
#         x = random.randint(10, 20)
#         request.session['gained'] += x
#         return redirect('/') 
#     elif y == 'cave':
#         x = random.randint(5, 10)
#         request.session['gained'] += x
#         return redirect('/') 
#     elif y == 'house':
#         x = random.randint(2, 5)
#         request.session['gained'] += x
#         return redirect('/') 
#     elif y == 'casino':
#         x = random.randint(0, 50)
#         request.session['gained'] += x
#         return redirect('/') 
#     return redirect('/')
