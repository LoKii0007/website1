from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import ProductType , Inquiry, Contact, Products

# Create your views here.

def home(request):
    producttypes= ProductType.objects.all()
    n =len(producttypes)
    params = {'no of cards':n, 'producttype':producttypes}


    return render(request, 'home.html', params)


def products(request):

    producttypes = ProductType.objects.all()
    n =len(producttypes)
    params = {'no of cards':n, 'producttype':producttypes}


    return render(request, 'products.html', params)


def productview(request, pid):

    # fetching that particular product type

    prodview = ProductType.objects.filter(product_id = pid)

    # fetching the products

    allprods =[]
    products = Products.objects.filter(product_id = pid)
    for product in products :
        allprods.append(product)

    return render(request, 'productview.html', {'prodview':prodview[0], 'allprod':allprods})
   

def handlesignup(request):
    if request.method == 'POST':

        # getting post parameters

        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers.")
            return redirect("/")
        

        if ( pass1 == pass2):

            if ( not pass1.isalnum()):
                messages.error(request, "Password should contain both numbers and letters.")
                return redirect("/")
            
            elif (len(pass1)<8):
                messages.error(request, "Password must be at least 8 characters long.")
                return redirect("/")

            elif(len(pass1)>=8 ):

                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name= fname
                myuser.last_name= lname
                myuser.save()
                messages.success(request , "your account has been succesfullt created")
                return redirect("/")
        
        else:
            messages.error(request, "your passwords did not match please type correct passwords")
            return redirect("/")
    
    else:
        return HttpResponse("404 - not found")
    

def handleLogin(request):

    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(email=loginusername,  username = loginusername, password= loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect("/")
        else:
            messages.error(request, "invalid credentials")
            return redirect("/")
    
    else:
        return HttpResponse("error 404")
    


def handleLogout(request):
    logout(request)
    messages.success(request, "successfully logged out")
    return redirect("/")


def handleInquiry(request):

    # fetching info from user

    if request.method == 'POST' :
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')

        inquirydetails = Inquiry(full_name = name, email = email, phone = phone, query =query)
        inquirydetails.save()

        messages.success(request, "Your query has been submitted. We will contact you soon")
        return redirect("/")
    

def contact(request):

    # fetching info from user


    if (request.method=="POST"):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        thank=True
        contact=Contact(name=name, phone = phone, description = desc, email=email )
        contact.save()

        return render(request, "contact.html",{'thank':thank})
   
    return render(request, "contact.html")

def location(request):
    return render(request, 'visit.html')
