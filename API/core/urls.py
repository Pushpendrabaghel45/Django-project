from django.urls import path
from .views import AdminLoginAPI, AdminDashboardAPI, AdminCreateEmployeeAPI, AdminViewEmployeeAPI


urlpatterns = [
    path('admin/login/', AdminLoginAPI.as_view(), name='admin_login'),
    path('admin/dashboard/', AdminDashboardAPI.as_view(), name='admin_dashboard'),
    path('admin/create-employee/', AdminCreateEmployeeAPI.as_view(), name='admin_createemp'),
    path('admin/employees/', AdminViewEmployeeAPI.as_view(), name='admin_viewempdetails'),
]







# {
#   "username": "admin",
#   "password": "adm@1234"
# }


# {
#   "first_name": "John",
#   "last_name": "Doe",
#   "email": "john.doe@gmail.com",
#   "phone": "9876543210",
#   "department": "IT",
#   "designation": "Software Engineer",
#   "address": "Delhi, India"
# }
