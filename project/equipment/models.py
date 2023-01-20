from django.db import models
from django import forms

class Equipment(models.Model):
    CAT_CHOICES = (
        ("Input Unit", "Input"),
        ("Processor Unit", "Processor"),
        ("Output Unit", "Output"),
    )
    eid = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=10)
    image = models.ImageField(upload_to='files/images')
    cat = models.CharField(max_length=50,
                            choices=CAT_CHOICES)

    def __str__(self):
        return self.eid

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        labels = {
            'eid' : 'Equipment Id',
            'cat' : 'Category',
            'name' : 'Name',
            'desc' : 'Description',
            'image': 'Images',
        }

