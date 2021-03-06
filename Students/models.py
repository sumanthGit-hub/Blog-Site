from django.db import models

# Create your models here.
class Student(models.Model):
    title=models.CharField(max_length=100)
    auth=models.CharField(max_length=100)
    file=models.FileField(upload_to='Students/files')
    cover=models.ImageField(upload_to='Students/cover/',null=True,blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args,**kwargs)