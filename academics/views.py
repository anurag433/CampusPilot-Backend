from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import SubjectSerializer ,AssignmentSerializer, ExamSerializer, NotesSerializer
from .models import Subject, Assignment, Exam, Notes

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Assignment.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Exam.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)