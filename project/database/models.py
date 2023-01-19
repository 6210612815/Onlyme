from django.db import models
from django import forms

class Student(models.Model):
    userId = models.CharField(max_length=50, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sid = models.CharField(max_length=10)
    tel = models.CharField(max_length=10)

    def __str__(self):
        return self.sid

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'userId' : 'userId',
            'fname' : 'fname',
            'lname' : 'lname',
            'email' : 'email',
            'sid' : 'sid',
            'tel' : 'tel'
        }

