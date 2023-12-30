
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import (Teacher, Subject, StudentProgress, Activity,
                     Resource, Coach, CoachTeacher, TeacherSubject,
                     ResourceTeacher)
from .serializers import (CoachSerializer, ResourceSerializer,
                         TeacherSerializer, SubjectSerializer,
                         StudentProgressSerializer,
                         ActivitySerializer, ResourceTeacherSerializer,
                         CoachTeacherSerializer, TeacherSubjectSerializer)
from rest_framework.views import status
from django.core import serializers


@api_view(['GET'])
def index(request):
    return Response({'index': True})


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def create(self, request): # Here is the new update comes <<<<
        data = request.data
        serializer = TeacherSerializer(data=data)
        m = Teacher.objects.filter(name=data['name']).first()
        if not m:
            if serializer.is_valid():
                m = serializer.save()
                ok_message = {'success': 'OK', 'message': "created", 'status_code': 201}
                return Response(ok_message)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_message = {'success': 'OK', 'message': "Aleady exists", 'status_code': 204}
            return Response(exist_message, status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        name = request.GET.get('name', '')
        if name:
            t = Teacher.objects.filter(name=name).first()
        return Response(t, status=status.HTTP_200_OK)

    def list(self, request):
        name = request.GET.get('name', '')
        q_teachers = request.GET.get('q_teachers', '')
        if name:
            t = Teacher.objects.filter(name=name).all()
        elif q_teachers:
            t = Teacher.objects.filter(name__contains=q_teachers).all()
        else:
            t = Teacher.objects.all()
        d = TeacherSerializer(t, many=True).data
        return Response(d, status=status.HTTP_200_OK)
    

class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    def create(self, request):
        data = request.data
        serializer = SubjectSerializer(data=data)
        m = Subject.objects.filter(name=data['name']).first()
        if not m:
            if serializer.is_valid():
                m = serializer.save()
                ok_message = {'success': 'OK', 'message': "created", 'status_code': 201}
                return Response(ok_message)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_message = {'success': 'OK', 'message': "Aleady exists", 'status_code': 204}
            return Response(exist_message, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        id = request.GET.get('id', '')
        if id:
            s = Subject.objects.filter(teacher=id).first()
        return Response(s, status=status.HTTP_200_OK)

    def list(self, request):
        name = request.GET.get('name', '')
        q_subjects = request.GET.get('q_subjects', '')
        if name:
            s = Subject.objects.filter(name=name).all()
        elif q_subjects:
            s = Subject.objects.filter(name__contains=q_subjects).all()
        else:
            s = Subject.objects.all()
        d = SubjectSerializer(s, many=True).data
        return Response(d, status=status.HTTP_200_OK)


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    def create(self, request): # Here is the new update comes <<<<
        data = request.data
        serializer = ActivitySerializer(data=data)

        m = Activity.objects.filter(teacher=data['teacher']).first()
        if not m:
            if serializer.is_valid():
                m = serializer.save()
                ok_message = {'success': 'OK', 'message': "created", 'status_code': 201}
                return Response(ok_message)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_message = {'success': 'OK', 'message': "Aleady exists", 'status_code': 204}
            return Response(exist_message, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        # your code
        return Response('serialized_data', status=status.HTTP_200_OK)

    def list(self, request):
        name = request.GET.get('name', '')
        q_teacher_activities = request.GET.get('q_teacher_activities', '')
        if name:
            a = Activity.objects.filter(name=name).all()
        elif q_teacher_activities:
            a = Activity.objects.select_related('teacher').filter(teacher__name__contains=q_teacher_activities).all()
        else:
            a = Activity.objects.all()
        d = ActivitySerializer(a, many=True).data
        return Response(d, status=status.HTTP_200_OK)


class StudentProgressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    serializer_class = StudentProgressSerializer
    queryset = StudentProgress.objects.all()
    def create(self, request): # Here is the new update comes <<<<
        data = request.data
        serializer = StudentProgressSerializer(data=data)
        m = StudentProgress.objects.filter(class_id=data['class_id']).first()
        if not m:
            if serializer.is_valid():
                m = serializer.save()
                ok_message = {'success': 'OK', 'message': "created", 'status_code': 201}
                return Response(ok_message)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_message = {'success': 'OK', 'message': "Aleady exists", 'status_code': 204}
            return Response(exist_message, status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        # your code
        return Response('serialized_data', status=status.HTTP_200_OK)

    def list(self, request):
        name = request.GET.get('name', '')
        q_student_progresses = request.GET.get('q_student_progresses', '')
        if name:
            sp = StudentProgress.objects.select_related('subject').filter(subject__name__contains=name).all()
        elif q_student_progresses:
            sp = StudentProgress.objects.select_related('subject').filter(subject__name__contains=q_student_progresses).all()
        else:
            sp = StudentProgress.objects.all()
        d = StudentProgressSerializer(sp, many=True).data
        return Response(d, status=status.HTTP_200_OK)


class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()
    def create(self, request): # Here is the new update comes <<<<
        data = request.data
        serializer = ResourceSerializer(data=data)
        m = Resource.objects.filter(id=data['id']).first()
        if not m:
            if serializer.is_valid():
                m = serializer.save()
                ok_message = {'success': 'OK', 'message': "created", 'status_code': 201}
                return Response(ok_message)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_message = {'success': 'OK', 'message': "Aleady exists", 'status_code': 204}
            return Response(exist_message, status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        # your code
        return Response('serialized_data', status=status.HTTP_200_OK)

    def list(self, request):
        name = request.GET.get('name', '')
        q_resources = request.GET.get('q_resources', '')
        if name:
            r = Resource.objects.filter(name=name).all()
        elif q_resources:
            r = Resource.objects.filter(name__contains=q_resources).all()
        else:
            r = Resource.objects.all()
        d = ResourceSerializer(r, many=True).data
        return Response(d, status=status.HTTP_200_OK)


class CoachViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()
    
    def create(self, request): # Here is the new update comes <<<<
        data = request.data
        serializer = CoachSerializer(data=data)
        m = Coach.objects.filter(id=data['id']).first()
        if not m:
            if serializer.is_valid():
                m = serializer.save()
                ok_message = {'success': 'OK', 'message': "created", 'status_code': 201}
                return Response(ok_message)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_message = {'success': 'OK', 'message': "Aleady exists", 'status_code': 204}
            return Response(exist_message, status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        # your code
        return Response('serialized_data', status=status.HTTP_200_OK)
        
    def list(self, request):
        name = request.GET.get('name', '')
        q_coaches = request.GET.get('q_coaches', '')
        if name:
            c = Coach.objects.filter(name=name).all()
        elif q_coaches:
            c = Coach.objects.filter(name__contains=q_coaches).all()
        else:
            c = Coach.objects.all()
        d = CoachSerializer(c, many=True).data
        return Response(d, status=status.HTTP_200_OK)


class ResourceTeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    serializer_class = ResourceTeacherSerializer
    queryset = ResourceTeacher.objects.all()

    def create(self, request):
        data = request.data
        serializer = ResourceTeacherSerializer(data=data)
        m = ResourceTeacher.objects.filter(
                resource=data['resource']).filter(
                teacher=data['teacher']).first()
        if not m:
            if serializer.is_valid():
                m = serializer.save()
                ok_message = {'success': 'OK', 'message': "created", 'status_code': 201}
                return Response(ok_message)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_message = {'success': 'OK', 'message': "Aleady exists", 'status_code': 204}
            return Response(exist_message, status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        # your code
        return Response('serialized_data', status=status.HTTP_200_OK)

    def list(self, request):
        queryset = ResourceTeacher.objects.all()
        d = ResourceTeacherSerializer(queryset, many=True).data
        return Response(d, status=status.HTTP_200_OK)


class CoachTeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    serializer_class = CoachTeacherSerializer
    queryset = CoachTeacher.objects.all()

    def create(self, request): # Here is the new update comes <<<<
        data = request.data
        serializer = CoachTeacherSerializer(data=data)
        m = CoachTeacher.objects.filter(
                    coach=data['coach']).filter(
                    teacher=data['teacher']).first()
        if not m:
            if serializer.is_valid():
                m = serializer.save()
                ok_message = {'success': 'OK', 'message': "created", 'status_code': 201}
                return Response(ok_message)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_message = {'success': 'OK', 'message': "Aleady exists", 'status_code': 204}
            return Response(exist_message, status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        # your code
        return Response('serialized_data', status=status.HTTP_200_OK)

    def list(self, request):
        queryset = CoachTeacher.objects.all()
        d = CoachTeacherSerializer(queryset, many=True).data
        return Response(d, status=status.HTTP_200_OK)


class TeacherSubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    serializer_class = TeacherSubjectSerializer
    queryset = TeacherSubject.objects.all()

    def create(self, request): # Here is the new update comes <<<<
        data = request.data
        serializer = TeacherSubjectSerializer(data=data)
        m = TeacherSubject.objects.filter(
                teacher=data['teacher']).filter(
                subject=data['subject']).first()
        if not m:
            if serializer.is_valid():
                m = serializer.save()
                ok_message = {'success': 'OK', 'message': "created", 'status_code': 201}
                return Response(ok_message)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_message = {'success': 'OK', 'message': "Aleady exists", 'status_code': 204}
            return Response(exist_message, status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        # your code
        return Response('serialized_data', status=status.HTTP_200_OK)

    def list(self, request):
        queryset = TeacherSubject.objects.all()
        d = TeacherSubjectSerializer(queryset, many=True).data
        return Response(d, status=status.HTTP_200_OK)

