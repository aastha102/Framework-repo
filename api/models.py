from django.db import models

# Create your models here.
class Student_API(models.Model):
    student_id = models.CharField(max_length = 10)
    student_name = models.CharField(max_length = 20)
    student_branch = models.CharField(max_length = 30)

    def __str__(self):
        return self.student_name

