from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentModelSerializer
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
    def get(self, request):
        student_id = request.query_params.get('id')

        # Gets all students data
        if student_id is None:
            student_queryset = Student.objects.all().order_by('id')

            serialized_data = StudentModelSerializer(
                student_queryset, many=True).data
            return Response({'students': serialized_data}, status=status.HTTP_200_OK)

        # Gets the single Student Data
        else:
            try:
                student = Student.objects.get(id=student_id)
                serialized_data = StudentModelSerializer(student).data
                return Response({"data": serialized_data}, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def post(self, request):
        try:
            student_req_body = request.data
            serialized_data = StudentModelSerializer(data=student_req_body)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response({"data": serialized_data.data}, status=status.HTTP_201_CREATED)
            else:
                # Return a response with validation errors
                return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle any other exceptions and return an appropriate response
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
            