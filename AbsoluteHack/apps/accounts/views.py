from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.http import Http404,HttpResponse,HttpRequest
from .forms import SignupForm,LoginForm
from rolepermissions.roles import assign_role
from .roles import NormalUser,SuperUser



#from django.contrib.auth.models import
# Create your views here.
def isUserLoggedIn(request):
    if user.request.is_authenticated:
        return HttpResponse(True)
    else:
        return HttpResonse(False)


def userLoginView(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email_id'], password=request.POST['password'])
            if user is not None :
                if user.email_confirmed == True:
                    login(request , user)
                    return redirect(request.GET.get('next') if request.GET.get('next', False) else settings.LOGIN_REDIRECT_URL)
                else:
                    form.add_error(None, "Your account isn't activated.")
            else:
                form.add_error(None,"No account exists with given email") 
    else:
        form = LoginForm()

    return render(request , 'accounts/login.html' , { 'form':form })                       








def userSignupView(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            assign_role(user , NormalUser)
            user = authenticate(email=request.POST['email_id'], password=request.POST['password'])
            if user is not None:
                if SendAccountActivationEmail(user.email):
                    return render(request, "success.html", {"message": "Account created successfully! Please check your email for activation email to activate your account."})
                else:
                    return render(request, "error.html", {"message": "Unable to send Account Activation Email. Contact Support."})

    else:
        form = SignupForm()        
            
    return render(request , 'accounts/signup.html' , { 'form':form } )




def LogoutView(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    logout(request)
    return redirect( settings.LOGIN_URL)




