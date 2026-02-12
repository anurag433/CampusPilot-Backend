from django.db import models
from django.conf import settings

class Subject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Subject_name = models.CharField(max_length=20)

    syllabus_image = models.ImageField(
        upload_to='syllabus/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

class Assignment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject ,on_delete= models.CASCADE)

    deadlines = models.DateField()
    assignment_pdf= models.FileField(
        upload_to='assignment/',
        null=True,
        blank=True
    )

    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Exam(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField()

    created_at = models.DateTimeField(auto_created=True)

class Notes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    notes= models.FileField(
        upload_to='notes/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_created=True)