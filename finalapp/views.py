from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from finalapp.models import Category
from finalapp.models import Foods
from finalapp.models import Events
from finalapp.models import Customer
from django.core.mail import send_mail
from finalapp.models import Eventbooking
from finalapp.models import Foodbooking
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'index.html')
def loginpg(request):
    return render(request,'login.html')
@login_required(login_url='login1')
def admpg(request):
    return render(request,'adminpanel.html')
def login1(request):
 if request.method == 'POST':
    username=request.POST['username']
    password=request.POST['password']
    user = auth.authenticate(username=username, password=password) 
    #request.session["uid"]=user.id#session method part
    if user is not None:
        if user.is_staff:
            login(request,user)
            messages.success(request,'Welcome Admin...')
            return redirect('addc')
        else:
            login(request,user)
            auth.login(request,user)
            messages.success(request,'Welcome Back...')
            return redirect('accountpg')
        
    else:
        messages.info(request,'Invalid Username or Password. Try again.')
        return redirect('home')
 else:
     return redirect('home')
@login_required(login_url='login1')
def logout(request):
    #if request.user.is_authenticated:(is authenticated method part)
    #request.session["uid"] = ""#session method part
    auth.logout(request)
    return redirect('home')
@login_required(login_url='login1')
def addc(request):
    return render(request,'addcategory.html')
@login_required(login_url='login1')
def addcdb(request):
    if request.method=="POST":
        c_name=request.POST.get('c_name')
        c_image=request.FILES.get('c_image')
        categoryz=Category(c_name=c_name,c_image=c_image)
        categoryz.save()
        return redirect('addc')
@login_required(login_url='login1')    
def showc(request):
    prod=Category.objects.all()
    return render(request,'showcategory.html',{'p':prod})
@login_required(login_url='login1')
def deletecat(request,pk):
    emp=Category.objects.get(id=pk)
    emp.delete()
    return redirect('showc')
@login_required(login_url='login1')
def addf(request):
   products=Category.objects.all()
   return render(request,'addfood.html',{'p':products})
@login_required(login_url='login1')#(login_required method part)
def addfdb(request):
    if request.method=='POST':
        f_name=request.POST['f_name']
        print(f_name)
        desc=request.POST['desc']
        print(desc)
        price=request.POST['price']
        print(price)
        opt=request.POST['opt']
        print(opt)
        qty=request.POST['qty']
        print(qty)
        f_image=request.FILES.get('f_image')
        print(f_image)
        cat=Category.objects.get(id=opt)
        print(cat)
        prod=Foods(f_name=f_name,desc=desc,price=price,f_image=f_image,qty=qty,category=cat)
        prod.save()
        return redirect('addf')
@login_required(login_url='login1')    
def showf(request):
    prod=Foods.objects.all()
    return render(request,'showfood.html',{'p':prod})
@login_required(login_url='login1')
def deletef(request,pk):
    emp=Foods.objects.get(id=pk)
    emp.delete()
    return redirect('showf')
@login_required(login_url='login1')
def adde(request):
    return render(request,'addevent.html')
@login_required(login_url='login1')
def addedb(request):
    if request.method=="POST":
        e_name=request.POST.get('e_name')
        e_image=request.FILES.get('e_image')
        categoryz=Events(e_name=e_name,e_image=e_image)
        categoryz.save()
        return redirect('adde')
@login_required(login_url='login1')     
def showe(request):
    prod=Events.objects.all()
    return render(request,'showevent.html',{'p':prod})
@login_required(login_url='login1')
def deletee(request,pk):
    emp=Events.objects.get(id=pk)
    emp.delete()
    return redirect('showe')
@login_required(login_url='login1')  
def editf(request,pk):
    food=Foods.objects.get(id=pk)
    cat=Category.objects.all()
    return render(request,'editfood.html',{'food':food,'category':cat})
@login_required(login_url='login1')#(login_required method part)
def editfdb(request,pk):
    if request.method=="POST":
        food=Foods.objects.get(id=pk)
        food.f_name=request.POST['f_name']
        
        food.desc=request.POST['desc']
        
        food.qty=request.POST['qty']
        
        food.price=request.POST['price']

        food.f_image=request.FILES.get('f_image')

        opt=request.POST['opt']
      
        cat1=Category.objects.get(id=opt)
        
        food.category=cat1
        food.save()
        return redirect('showf')  
    return render(request,'editfood.html') 
def signup(request):
    return render(request,'signup.html') 
def signupdb(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name') 
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        address=request.POST.get('address')
        email=request.POST.get('email')
        number=request.POST.get('number')
        age=request.POST.get('age')
        image=request.FILES.get('image')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists !!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
                u=User.objects.get(id=user.id)

                member=Customer(address=address,number=number,age=age,image=image,userc=u)
                member.save()

                subject="USERNAME AND PASSWORD"
                message=f'your username is {username} and password is {password}'           
                send_mail(subject,message,settings.EMAIL_HOST_USER,[email])

                return redirect('/')
        else:
            messages.info(request,'Password does match !!!')
            return redirect('signup')
    else:
        return render(request,'signup.html')
@login_required(login_url='login1')      
def showu(request):
    use=Customer.objects.all()
    return render(request,'showuser.html',{'u':use}) 
@login_required(login_url='login1')
def deleteu(request,pk):
    emp=Customer.objects.get(id=pk)
    emp.delete()
    return redirect('showu')
@login_required(login_url='login1')
def userpg(request):
    return render(request,'userpanel.html')
@login_required(login_url='login1')
def accountpg(request):
    ucuser=request.user.id
    u=Customer.objects.get(userc_id=ucuser)
    return render(request, 'account.html',{'usrkey':u})
@login_required(login_url='login1')
def eventbooking(request):
   products=Events.objects.all()
   food=Foods.objects.all()
   context={'p':products,'f':food}
   return render(request,'bookingevent.html',context)
@login_required(login_url='login1')
def eventbookingdb(request):
    
    if request.method=='POST':
        user_id=request.user.id
        user=Customer.objects.get(userc=user_id)
        
        date=request.POST['date']
        time=request.POST['time']
        venue=request.POST['place']
        people=request.POST['people']
        select1=request.POST['select1']
        eventpack=Events.objects.get(id=select1)
        select2=request.POST['select2']
        menupack=Foods.objects.get(id=select2)
        amount=request.POST.get('amount')

        bookings=Eventbooking(date=date,time=time,venue=venue,people=people,eventpack=eventpack,menupack=menupack,user=user,amount=amount)
        bookings.save()
        messages.warning(request,'Your Booking request is received,please wait for confirmation')
        return redirect('eventbooking')
@login_required(login_url='login1')    
def bookinglist(request):
    
    user_id=request.user.id
    user1=Customer.objects.get(userc=user_id)
    bookinglist=Eventbooking.objects.filter(user=user1)
    foodlist=Foodbooking.objects.filter(user=user1)
    event=Events.objects.all()
    menu=Foods.objects.all()
    cat=Category.objects.all()

    context={'bookinglist':bookinglist,'foodlist':foodlist,'event':event,'menu':menu,'cat':cat}
    return render(request,'showbooking.html',context)
@login_required(login_url='login1')
def deleteevent(request,pk):
    
    bookinglist=Eventbooking.objects.filter(id=pk)
    bookinglist.delete()
    messages.warning(request,'Deleted')
    return redirect('bookinglist')
@login_required(login_url='login1')
def foodbooking(request):
   cat=Category.objects.all()
   food=Foods.objects.all()
   context={'c':cat,'f':food}
   return render(request,'bookingfood.html',context)
@login_required(login_url='login1')
def foodbookingdb(request):
    
    if request.method=='POST':
        user_id=request.user.id
        user=Customer.objects.get(userc=user_id)
        
        date=request.POST['date']
        time=request.POST['time']
        
        people=request.POST['people']
        select1=request.POST['select1']
        catpack=Category.objects.get(id=select1)
        select2=request.POST['select2']
        menupack=Foods.objects.get(id=select2)
        

        bookings=Foodbooking(date=date,time=time,people=people,catpack=catpack,menupack=menupack,user=user)
        bookings.save()
        messages.warning(request,'Your Booking request is received,please wait for confirmation')
        return redirect('foodbooking')
@login_required(login_url='login1')   
def eventrequest(request):
    if not request.user.is_staff:
        return redirect('/login')
    pendingbookings=Eventbooking.objects.filter(approved=False,reason=None)
    pendingbooking=Foodbooking.objects.filter(approved=False,reason=None)
    context={'pendingbookings':pendingbookings,'pendingbooking':pendingbooking}
    return render(request,'showusrbook.html',context)
@login_required(login_url='login1') 
def approve(request, pk):
    
    booking = Eventbooking.objects.get(id=pk)
    booking.approved = True
    booking.save()
    messages.success(request,'Event Booking Confirmed')
    return redirect('eventrequest')

@login_required(login_url='login1')
def approvef(request, pk):
    
    booking = Foodbooking.objects.get(id=pk)
    booking.approved = True
    booking.save()
    messages.success(request,'Food Booking Confirmed')
    return redirect('eventrequest')
@login_required(login_url='login1')
def rejectf(request, pk):
    if request.method=='POST':
        reason=request.POST.get('reason')
        events=Foodbooking.objects.get(id=pk)
        events.approved=False
        events.reason=reason
        events.save()
        return redirect('eventrequest')  
    return render(request,'rejectreason.html')
@login_required(login_url='login1')
def reject(request, pk):
    if request.method=='POST':
        reason=request.POST.get('reason')
        events=Eventbooking.objects.get(id=pk)
        events.approved=False
        events.reason=reason
        events.save()
        return redirect('eventrequest')
    return render(request,'rejectreason.html')
@login_required(login_url='login1') 
def approvedbookings(request):
    approvedbookings=Eventbooking.objects.filter(approved=True, completed=False)
    approvedbooking=Foodbooking.objects.filter(approved=True, completed=False)
    context={'approvedbookings':approvedbookings,'approvedbooking':approvedbooking}
    return render(request,'approvedbookings.html',context)   

    