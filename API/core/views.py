from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from core.models import Employee
from .serializers import LoginSerializer, EmployeeSerializer


# Admin Login API .........
class AdminLoginAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user and user.is_staff:
            login(request, user)
            return Response({
                "message": "Admin login successful",
                "username": user.username
            })
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )



# Dashboard API .........

class AdminDashboardAPI(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        total_employees = Employee.objects.count()
        return Response({
            "message": "Welcome to Admin Dashboard",
            "total_employees": total_employees
        })


# Create Employee API .........
class AdminCreateEmployeeAPI(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Employee created", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  View Employee Details API ...........
class AdminViewEmployeeAPI(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

