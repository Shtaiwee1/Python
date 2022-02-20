from django.shortcuts import render , redirect
from .models import User , Book
from django.contrib import messages
import bcrypt


def index(request):
        users = User.objects.all()
        context = {
            'all_users': users,
        }
        return render(request, 'index.html',context)
    
def process_reg(request):
    errors = User.objects.basic_validator(request.POST)#passes the data from form to the validators function in models which are then called (postData)-validates and then returns errors from the models page
    request.session["coming_from"]="REGISTER"
    if len(errors) > 0:#if there are errors loop through keys and values in the errors dictionary
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        request.session['first_name']=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user=User.objects.create(first_name=request.session['first_name'],
                                        last_name=last_name,
                                        email=email,
                                        password=hashed_password)
        return redirect('/books')
    
def process_login(request):
    errors = User.objects.basic_validator_second(request.POST)
    request.session["coming_from"]="LOGIN"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        find_user=User.objects.filter(email=request.POST['email_login'])
        if find_user:
            logged_user = find_user[0]
            if bcrypt.checkpw(request.POST['password_login'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                request.session['first_name'] = logged_user.first_name
                request.session['last_name'] = logged_user.last_name
                request.session['email'] = logged_user.email
                return redirect('/books')
        return redirect('/')
    
def books_page(request):
    if "email" not in request.session:
        return redirect('/')
    log_user=User.objects.get(first_name=request.session['first_name'])
    context={"current_user":log_user,
            "all_users":User.objects.all(),
            "all_books":Book.objects.all(),
            }
    return render(request,'books.html',context)
    
def add_fav_book(request):
    errors = Book.objects.basic_validator_book(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        book_title=request.POST['title']
        book_desc=request.POST['desc']
        this_user=User.objects.get(id=request.session['user_id'])
        this_book=Book.objects.create(title=book_title,desc=book_desc,uploaded_by=this_user)
        this_book.users_who_like.add(this_user)
        return redirect(f"/books/{this_book.id}")
        
def edit_show_book(request , book_id ):
    this_user=User.objects.get(id=request.session['user_id'])
    this_book=Book.objects.get(id=book_id)
    book_uploader=this_book.uploaded_by.id
    user_like_book=this_book.users_who_like.all()
    if book_uploader==this_user.id:
        print(user_like_book)
        context={"books":this_book,
            "current_user":this_user,
            "liked_by":user_like_book,}
        return render(request,'edit_book.html',context)
    else:
        print(user_like_book)
        context={"books":this_book,
            "current_user":this_user,
            "liked_by":user_like_book}
        return render(request,'show_book.html',context)
    
def clear(request):
    request.session.clear()
    return redirect('/')

def update_info(request,book_id):
    errors = Book.objects.basic_validator_book(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            this_book=Book.objects.get(id=book_id)
            return redirect(f"/books/{this_book.id}")   
    if request.POST.get('submit_button')=='update':
        update_book=Book.objects.get(id=book_id)
        update_book.title=request.POST['title']
        update_book.desc=request.POST['desc']
        update_book.save()
    elif request.POST.get('submit_button')=='delete':
        delete_book=Book.objects.get(id=book_id)
        delete_book.delete()
    return redirect('/books')

def fav_book(request,book_id,user_id):
    this_user=User.objects.get(id=user_id)
    this_book=Book.objects.get(id=book_id)
    this_book.users_who_like.add(this_user)
    return redirect(f'/books/{book_id}')

def unfav_book(request,book_id,user_id):
    this_user=User.objects.get(id=user_id)
    this_book=Book.objects.get(id=book_id)
    this_book.users_who_like.remove(this_user)
    return redirect(f'/books/{book_id}')


