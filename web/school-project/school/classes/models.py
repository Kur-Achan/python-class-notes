from django.db import models

# Create your models here.
class  Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=40)
    class_description = models.TextField()
    class_start_date = models.DateField()
    class_end_date = models.DateField()
    class_capacity = models.IntegerField()
    class_status = models.CharField(max_length=10)
    class_location = models.CharField(max_length=35)
    class_time = models.CharField(max_length=15)
    class_students = models.ManyToManyField('Student')
    def __str__(self):
        return f"{self.class_name}"