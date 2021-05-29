from django.shortcuts import render
from django.contrib import  messages
from .models import Contact ,addblog
from django.contrib import  messages
from django.core.paginator import Paginator

# --------------- MAIN WEB PAGES -----------------------------

def index(request):

	return render(request, 'index.html')
	 

def project(request):
    data = addblog.objects.all()
    paginator = Paginator(data, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'projects.html',{'page_obj': page_obj})
    
def blog(request):
    data = addblog.objects.all()
    paginator = Paginator(data, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html',{'page_obj': page_obj})

def addblogs(request):
    data = addblog.objects.all()
    paginator = Paginator(data, 25)
    blog = {"sno": data}
    return render(request, 'addblog.html',blog)

def contact(request):
    if request.method=="POST":
        F_name=request.POST['F_name']
        L_name=request.POST['L_name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(F_name)<2 or len(L_name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(F_name=F_name,L_name=L_name , email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'contact.html')

# -----------------------------------------------------------