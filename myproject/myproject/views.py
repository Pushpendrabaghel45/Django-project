from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# home 

def home(request):
    return render(request, "home.html")



# signup 


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')


#  Login (SAFE) 

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


# Protected Pages (Login Required)



@login_required
def index(request):
    return render(request, "index.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def about_us(request):
    return render(request, "about_us.html")

@login_required
def our_services(request):
    return render(request, "our_services.html")

@login_required
def testimonials(request):
    return render(request, "testimonials.html")


@login_required
def contact_us(request):
    return render(request, "contact_us.html")

@login_required
def register(request):
    return render(request, "register.html")

@login_required
def userform(request):
    return render(request, "userform.html")




# --- LOGOUT ----
def user_logout(request):
    auth_logout(request)
    return redirect('login')

# def index(request):
#     data = {
#         'n1': request.GET.get('n1'),
#         'n2': request.GET.get('n2'),
#         'n3': request.GET.get('n3'),
#         'n4': request.GET.get('n4'),
#     }
#     return render(request, "index.html", data)

# def about_us(request):
#     return render(request, "about_us.html")





# from urllib.parse import urlencode

# def contact_us(request):
#     if request.method == "POST":
#         try:
#             n1 = request.POST.get("username")
#             n2 = request.POST.get("email")
#             n3 = request.POST.get("message")
#             n4 = request.POST.get("password")

#             params = urlencode({
#                 'n1': n1,
#                 'n2': n2,
#                 'n3': n3,
#                 'n4': n4,
#             })

#             return HttpResponseRedirect('/home?' + params)

#         except Exception as e:
#             print("Error:", e)

#     return render(request, "contact_us.html")



# def our_services(request):
#     return render(request, "our_services.html")





# def register(request):
    
#     if request.method == "POST":
#         try:
#             n1 = request.POST.get("username")
#             n2 = request.POST.get("email")
#             n3 = request.POST.get("message")
#             n4 = request.POST.get("password")

#             params = urlencode({
#             'n1': n1,
#             'n2': n2,
#             'n3': n3,
#             'n4': n4,
#              })

#             return HttpResponseRedirect('/contact_us?' + params)

#         except Exception as e:
#             print("Error:", e)

#     return render(request, "register.html")


# def userform(request):
#     result = 0
#     data = {}
#     try:
#         if request.method == "POST":
#             n1 = int(request.POST.get('num1'))
#             n2 = int(request.POST.get('num2'))
#             result = n1 + n2

#             data = {
#                 'n1': n1,
#                 'n2': n2,
#                 'output': result
#             }

#             url = '/contact_us?output={}'.format(result) 
#             return HttpResponseRedirect(url)
#     except:
#         pass

#     return render(request, "userform.html", data)

# def dashboard(request):
#     if request.method == "GET":
#         output = request.GET.get('output')
#     return render(request, "dashboard.html",  {'output': output})








# def contact_us(request):
#     if request.method == "GET":
#         output = request.GET.get('output')
#     # data = {
#     #     'n1': request.GET.get('n1'),
#     #     'n2': request.GET.get('n2'),
#     #     'n3': request.GET.get('n3'),
#     #     'n4': request.GET.get('n4'),
#     # }
#     return render(request, "contact_us.html", {'output': output})


# def ragister(request):
#     result = 0
#     data = {}
#     try:
#         if request.method == "POST":
#             p1 = str(request.POST.get('username'))
#             p2 = str(request.POST.get('email'))
#             p3 = str(request.post.get('message'))
#             result = p1, p2, p3

#             data = {
#                 'p1': p1,
#                 'p2': p2,
#                 'p3': p3,
#                 'output': result
#             }

#             url = '/dashboard?output={}'.format(result) 
#             return HttpResponseRedirect(url)
    # except:
        # pass
    # return render(request, "ragister.html", data)