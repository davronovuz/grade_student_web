from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class CustomUser(AbstractUser):

    class UserType(models.TextChoices):
        STUDENT="STUDENT","STUDENT"
        TEACHER="TEACHER","TEACHER"

    user_type=models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.STUDENT
    )

class Subject(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False,unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    student=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    subjects=models.ManyToManyField(Subject,related_name="students")


    def __str__(self):
        return f"{self.student}-{self.subjects}"


class Teacher(models.Model):
    teacher=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    subjects=models.ManyToManyField(Subject,related_name="teachers")


    def __str__(self):
        return f"{self.teacher}-{self.subjects}"



class Grade(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='grades')
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    grade=models.IntegerField(
        validators=[
            MinValueValidator(1,"2 dan katta baho qo'ying"),
            MaxValueValidator(5,"5 dan kichik baho qo'ying")
        ]
    )
    date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)



    def __str__(self):
        return f"{self.student}-{self.subject}-{self.grade}-{self.teacher}"









