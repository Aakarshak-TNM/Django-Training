from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from .models import Student, Standard
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentModelSerializer, StudentModelSerializerPost
import string
from urllib.parse import unquote
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
        query_param = request.query_params.get('query', None)
# "s"
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
