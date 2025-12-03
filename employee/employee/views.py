from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data= {
        'title': 'My Website',
        'greeting': 'Namaste bharat',
        'course_list': ['Fronted', 'Backend', 'Data Analysis', 'UI/UX'],
        'students_details': [
            {'name': 'rohan', 'phone': '8552222452'},
            {'name': 'sohan', 'phone': '8422222452'}
        ],
        'numbers': [10, 20, 30, 40, 50, 60, 70] 
    }

    return render(request, "index.html", data)

def about(request):
    context= {
        'username': 'pushpendra',
        'skills': ['python', 'django', 'flask', 'mysql']
    }
    return render(request, "about.html", context)

def team(request):
    return render(request, "team.html")

# def home(request):
#     return HttpResponse("Welcome To The Home Page.")

# def about(request):
#     return HttpResponse("Welcome To The about Page.")

# def team(request):
#     return HttpResponse("Welcome To The team Page.")

def teamdetails(request, teamid):
    return HttpResponse(teamid)