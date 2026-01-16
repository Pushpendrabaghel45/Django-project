from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from core.models import Employee
from .serializers import LoginSerializer, EmployeeSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.contrib.auth.models import User






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





# Dashboard API .........

class AdminDashboardAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({
            "message": "Employee list access granted",
            "admin": request.user.username
        })



# Create Employee API .........

class CreateEmployeeAPI(APIView):

    def post(self, request):
        email = request.data.get("email")

        # ✅ Check if user already exists
        if User.objects.filter(username=email).exists():
            return Response(
                {"error": "Employee with this email already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=email,
            email=email,          
            first_name=request.data.get("first_name"),
            last_name=request.data.get("last_name")
        )

        # create employee profile here
        Employee.objects.create(
            user=user,
            phone=request.data.get("phone"),
            department=request.data.get("department"),
            designation=request.data.get("designation"),
            address=request.data.get("address"),
        )

        return Response(
            {"message": "Employee created successfully"},
            status=status.HTTP_201_CREATED
        )

#  View Employee Details API ...........

class EmployeeListAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

