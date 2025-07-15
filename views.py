from django.shortcuts import render,redirect
from.models import*
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request,'index.html') 

def login(request):
    return render(request,'login.html') 

def registration(request):
    return render(request,'registration.html') 

def register(request):
    log=Login()
    log.username=request.POST.get("username")
    log.password=request.POST.get("password")
    log.usertype="user"
    log.status="Approved"
    log.save()

    obj=UserInfo()
    obj.name=request.POST.get("name")
    obj.address=request.POST.get("address")
    obj.phone_number=request.POST.get("phone")
    obj.email=request.POST.get("email")
    obj.login=log
    obj.save()
    messages.add_message(request, messages.INFO, 'Registered successfully.')
    return redirect('registration')



def login_action(request):
    u = request.POST.get("username")
    p = request.POST.get("password")

    obj = authenticate(username=u, password=p)
    if obj is not None:
        if obj.is_superuser == 1:
            request.session['aname'] = u
            request.session['slogid'] = obj.id
            return redirect('admin_home')
        else:
            messages.add_message(request, messages.INFO, 'Invalid User.')
            return redirect('login')
    else:
        obj1 = Login.objects.get(username=u, password=p)
        if obj1.usertype == "user":
            if obj1.status == "Approved":
                request.session['uname'] = u
                request.session['slogid'] = obj1.login_id
                return redirect('user_home')
            elif obj1.status == "Not Approved":
                messages.add_message(request, messages.INFO, 'Waiting For Approval.')
                return redirect('login')
            else:
                messages.add_message(request, messages.INFO, 'Invalid User.')
                return redirect('login')
        else:
            messages.add_message(request, messages.INFO, 'Invalid User.')
            return redirect('login')
     

    



def admin_home(request):
    if 'aname' in request.session:
        return render(request, 'Master/index.html')
    else:
      return redirect('login')
    


    
def userlist(request):
    if 'aname' in request.session:
        data=UserInfo.objects.all()
        return render(request, 'Master/userlist.html',{'userdata':data})
    else:
      return redirect('login')
    


def user_home(request):
    if 'uname' in request.session:
        return render(request, 'User/index.html')
    else:
      return redirect('login')
    


def addbook(request):
    if 'aname' in request.session:
        if request.method == 'POST':
            obj = Book()
            obj.bookname = request.POST.get("bookname")
            obj.author = request.POST.get("author")
            obj.description = request.POST.get("description")
            obj.price = request.POST.get("price")
            obj.save()
            messages.add_message(request, messages.INFO, 'Book added succesfully')
            return render(request, 'Master/addbook.html')
        return render(request, 'Master/addbook.html')
    else:
        return redirect('login')

    


def booklist(request):
    if 'aname' in request.session:  
        data=Book.objects.all()
        return render(request, 'Master/booklist.html',{'books':data})
    else:
      return redirect('login')
        
        

def logout_view(request):
    logout(request)  
    request.session.flush() 
    return redirect('login') 
 
