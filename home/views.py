from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from .models import Student, Standard
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentModelSerializer, StudentModelSerializerPost, StandardModelSerializerPost
import string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def navbar(request):
    # return HttpResponse("Hello World")
    return render(request, "home/navbar.html")


def contact(request):
    # return HttpResponse("Hello World")
    return render(request, "home/contact.html")


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentModelApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        student_id = request.query_params.get('id')
        query_param = request.query_params.get('query', None)
# "s"
        if not user.is_staff:
            return Response({"error": "You are not authorized to access this resource"}, status=status.HTTP_403_FORBIDDEN)
        else:
            if (query_param is not None):
                try:
                    for query in query_param:
                        if (query in string.ascii_letters):
                            query_param = query
                    student_data = Student.objects.filter(
                        name__contains=query_param)
                    student_serializer = StudentModelSerializer(
                        student_data, many=True).data
                    return Response({'data': student_serializer}, status=status.HTTP_200_OK)
                except Exception as e:
                    e = str(e)
                    return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)
            if student_id is None:
                student_queryset = Student.objects.all().order_by('id')
                serialized_data = StudentModelSerializer(
                    student_queryset, many=True).data
                return Response({'students': serialized_data}, status=status.HTTP_200_OK)
            else:
                try:
                    student = Student.objects.get(id=student_id)
                    serialized_data = StudentModelSerializer(student).data
                    return Response({"data": serialized_data}, status=status.HTTP_200_OK)
                except Student.DoesNotExist:
                    return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def post(self, request):
        student_data = request.data
        print(student_data)
        student_data['standard_name'] = Standard.objects.get(
            standard_name=student_data['standard_name']).id
        serializer = StudentModelSerializerPost(data=student_data)
        try:
            if serializer.is_valid():
                serializer.save()
                id = (serializer.data['id'])
                student_instance = Student.objects.get(id=id)
                student = StudentModelSerializer(student_instance)
                return Response(student.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        student_id = request.query_params.get('id')
        if student_id is not None:
            try:
                student_req_body = request.data
                student = Student.objects.get(id=student_id)
                student.name = student.name if student_req_body[
                    'name'] == '' else student_req_body['name']
                student.standard = student.standard if student_req_body[
                    'standard'] == '' else student_req_body['standard']
                student.standard_name.standard_name = student.standard_name.standard_name if student_req_body[
                    'standard_name'] == '' else student_req_body['standard_name']
                student.course = student.course if student_req_body[
                    'course'] == '' else student_req_body['course']
                student.save()
                serialized_data = StudentModelSerializer(student).data
                return Response({"data": serialized_data}, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        student_id = request.query_params.get('id')
        if student_id is not None:
            try:
                student = Student.objects.get(id=student_id)
                student.delete()
                return Response({"data": "Student is Deleted Succesfully"}, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                student = Student.objects.all()
                student.delete()
                return Response({"data": "Students is Deleted Succesfully"}, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)


class SignUpAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user_type = request.data.get('user_type')

        if not username or not email or not password or not user_type:
            return Response({'error': 'Please provide username, email, password, and user_type'}, status=400)

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return Response({'error': 'Username or email already exists'}, status=400)

        if user_type not in ['teacher', 'student']:
            return Response({'error': 'Invalid user_type. Must be "teacher" or "student"'}, status=400)

        # Create user based on user_type
        if user_type == 'teacher':
            user = User.objects.create_user(username, email, password)
            # Additional logic specific to teachers
            user.is_staff = True  # Make teacher a staff user
            user.save()
        elif user_type == 'student':
            user = User.objects.create_user(username, email, password)
            # Additional logic specific to students
            user.is_staff = False  # Make student a non-staff user
            user.save()
        return Response({'message': 'Signup successful'}, status=201)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = username
        if not username or not password:
            return Response({'error': 'Please provide username or email and password'}, status=400)
        if authenticate(username=username, password=password) == None:
            try:
                user = User.objects.get(email=email)
                user.last_login = timezone.now()
                user.save()
                refresh = RefreshToken.for_user(user)
                token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                if user.check_password(password):
                    return Response({'message': 'Login successful', 'token': token}, status=200)
                else:
                    return Response({'error': 'Invalid email or password'}, status=401)
            except User.DoesNotExist:
                return Response({'error': 'User with this email does not exist'}, status=401)
        else:
            user = authenticate(username=username, password=password)

            user.last_login = timezone.now()
            user.save()
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            if user is not None:
                return Response({'message': 'Login successful', 'token': token}, status=200)
            else:
                return Response({'error': 'Invalid username or password'}, status=401)


class StandardModelApiView(APIView):
    @csrf_exempt
    def post(self, request):
        standard_data = request.data
        standard_name = standard_data
        serializer = StandardModelSerializerPost(data=standard_name)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
