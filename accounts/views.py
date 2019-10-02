from django.shortcuts import render , redirect
from django.contrib.auth.models import auth , User
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']
        if pass1 != pass2:
            return render(request,'register.html',{'message':"Password doesn't match!"})
        else:
            if User.objects.filter(username=username).exists():
                print(username + " here")
                return render(request,'register.html',{'message':"Sorry! username already taken."})
            elif User.objects.filter(email=email).exists():
                return render(request,'register.html',{'message':"Email already exist in our system."})
            else:
                user = User.objects.create_user(username=username,email=email,password=pass1,first_name=firstname,last_name=lastname)
                user.save()
                return redirect('login')
    else:
        return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        print("ok")
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            print("yes")
            auth.login(request,user)
            return redirect('/')
        else:
            print('no')
            return render(request,'signin.html',{'message':'INVALID CREDENTIALS'})
    else:
        return render(request,'signin.html')

def signout(request):
    auth.logout(request)
    return redirect('/')
