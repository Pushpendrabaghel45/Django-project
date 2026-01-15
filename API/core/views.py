from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from core.models import Employee
from .serializers import LoginSerializer, EmployeeSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated


# Admin Login API .........



class AdminLoginAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = authenticate(
            username=request.data["username"],
            password=request.data["password"]
        )

        if user and user.is_staff:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            })

        return Response({"error": "Invalid credentials"}, status=401)


# class AdminLoginAPI(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = authenticate(
#             username=serializer.validated_data['username'],
#             password=serializer.validated_data['password']
#         )

#         if user and user.is_staff:
#             login(request, user)
#             return Response({
#                 "message": "Admin login successful",
#                 "username": user.username
#             })
#         return Response(
#             {"error": "Invalid credentials"},
#             status=status.HTTP_401_UNAUTHORIZED
#         )



# Dashboard API .........

class AdminDashboardAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({
            "message": "Employee list access granted",
            "admin": request.user.username
        })

# class AdminDashboardAPI(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, request):
#         return Response({
#             "username": request.user.username,
#             "role": "Admin",
#             "total_employees": 25
#         })

# Create Employee API .........
class EmployeeProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        employee = user.employee  # OneToOne relation

        return Response({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": employee.phone,
            "department": employee.department,
            "designation": employee.designation,
            "address": employee.address,
        })

    def put(self, request):
        user = request.user
        employee = user.employee

        user.first_name = request.data.get("first_name")
        user.last_name = request.data.get("last_name")
        user.email = request.data.get("email")
        user.save()

        employee.phone = request.data.get("phone")
        employee.address = request.data.get("address")
        employee.save()

        return Response({"message": "Profile updated"})
    



#  View Employee Details API ...........

class EmployeeDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        emp = request.user.employee

        return Response({
            "name": f"{request.user.first_name} {request.user.last_name}",
            "designation": emp.designation,
            "emp_id": emp.emp_id,
            "email": request.user.email,
            "phone": emp.phone,
            "department": emp.department,
            "joining_date": emp.joining_date,
            "status": emp.status,
        })

