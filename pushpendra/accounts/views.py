from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from .forms import CustomUserCreationForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to homepage")


# -----------------------------
# Signup
# -----------------------------
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


# -----------------------------
# Profile Page
# -----------------------------
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


# -----------------------------
# Logout
# -----------------------------
def logout_view(request):
    auth_logout(request)
    return redirect('login')


# -----------------------------
# Admin Dashboard
# -----------------------------
def is_admin(user):
    return user.groups.filter(name='AdminGroup').exists()


@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')