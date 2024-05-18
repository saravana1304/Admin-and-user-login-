from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Natural
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True) #performimg the sessions control,not ot redirect to older pages
@login_required(login_url='/login')#this means without loging in u cant perform this task nd logging i must
def index(request):
    dict_card = {
        'card': Natural.objects.all()
    }
    return render(request,'index.html', dict_card)
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)        
def login(request):
    if request.user.is_authenticated:#it checks whether the user is already loged in or not,123.8000/login/-if u
        return redirect(index)# give then it will redirect to the index rether than wasting time on loggign in one more time
    if request.method == 'POST':#if method is post only then it will enter inside
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)#checkes wether the username adn email is equal to the DB details
        if user is not None:#if user is not empty then it will redirect to index
            auth.login(request, user)#without auth we cannot log in or redirct ot the  index page.
            return redirect(index) 
        else:#if user is empty then u have to log in one more time
            messages.info(request,'User Name or Password is Incorrect')  
            return redirect(login)
    else:
        return render(request, "login.html")   
       
@cache_control(no_cache=True,must_revalidate=True,no_store=True)            
@login_required(login_url='/login') 
def logout(request):
    auth.logout(request)            
    return redirect(login)  


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def signup(request,verify):#2 para cause in admin also we r using signup thing
    if request.method == 'POST':
        if request.POST['username']!='':#checks wether username is empty or not
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            confirmpass = request.POST['confirmpass']
            if password == confirmpass:#checks wether the both pass r correct
                if User.objects.filter(username=username).exists():#will check wether entered username is already existing in the DB 
                    messages.info(request,'Username is already eixst')
                    return redirect(signup,1)
                else:
                    user = User.objects.create_user(email=email,username=username,password=password)
                    user.save()
                    if verify==1:
                        return redirect(adminn)
                return redirect(index)
            else:
                messages.info(request,'Password do not match')
                return redirect(signup,0)
        else:
            messages.info(request,'some field is empty')
            return redirect(signup,0)
    else:
        return render(request,'signup.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)            
@login_required(login_url='/login')      
def adminn(request):           
    if not request.user.is_superuser:           
        return redirect(index)           
    if request.method == 'POST':            
        search = request.POST['search']         
        searchresult = User.objects.filter(username__contains=search)           
        return render(request,'search.html',{'result':searchresult})          
                
    else:           
        dict_user={
            'users':User.objects.all().order_by('id')
        }
        return render(request,'admin.html',dict_user)
   

def delete_record(request,user_id):
    del_record = User.objects.filter(id=user_id)
    del_record.delete()
    return redirect(adminn)


def update_record(request,user_id):
    username=request.POST['username']
    email=request.POST['email']
    update_user = User.objects.filter(id=user_id)
    # update_user.update(username=username,email=email)

    if User.objects.filter(username__contains=username).exists():
        return redirect(adminn)
    else:
        update_user.update(username=username,email=email)
        return redirect(adminn)
    