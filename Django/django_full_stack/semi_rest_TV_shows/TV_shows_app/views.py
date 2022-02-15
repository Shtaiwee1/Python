from django.shortcuts import render , redirect 
from django.contrib import messages
from .models import Show
import datetime

def index(request):
    return redirect('/shows')

def allshows(request):
    context={
        "all_shows":Show.objects.all(),
    }
    return render(request, "index.html",context)

def new_show_form(request):
    return render(request, "addshow.html")

def addshow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new') 
    else:     
        title=request.POST['title']
        network=request.POST['network']
        desc=request.POST['desc']
        release_date=request.POST['date']
        current_show=Show.objects.create(title=title,
                            network=network,
                            desc=desc,
                            release_date=release_date)
        return redirect(f"/shows/{current_show.id}")

def edit_show_form(request,show_id):
    this_show=Show.objects.get(id=show_id)
    theshow={"current_show": this_show }
    return render(request, "editshow.html",theshow )

def editnewshow(request , show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/load")
    else:
        this_show=Show.objects.get(id=show_id)
        this_show.title=request.POST['title']
        this_show.network=request.POST['network']
        this_show.release_date=request.POST['date']
        this_show.desc=request.POST['desc']
        this_show.save()
    return redirect(f"/shows/{show_id}")

def showdetails(request,show_id):
    this_show_details=Show.objects.get(id=show_id)
    context={"show_details": this_show_details}
    return render(request, "showdetails.html",context)

def delete_show(request,show_id):
    erase_this=Show.objects.get(id=show_id)
    erase_this.delete()
    return redirect("/")

    
        
    

    

