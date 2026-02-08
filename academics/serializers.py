from rest_framework import serializers
from .models import Subject, Assginment , Exam, Notes

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ['user']

class AssginmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assginment
        fields = '__all__'
        read_only_fields = ['user']

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"
        read_only_fields = ['user']


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
        read_only_fields = ['user']