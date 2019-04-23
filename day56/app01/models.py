from django.db import models

# Create your models here.


# Create your models here.
class Classes(models.Model):

    title=models.CharField(max_length=32)
    m=models.ManyToManyField('Teachers')


class Teachers(models.Model):
    '''
    教师表
    '''
    name=models.CharField(max_length=32)



class Students(models.Model):
    username=models.CharField(max_length=32)
    age=models.IntegerField()
    gender=models.BooleanField()
    cs=models.ForeignKey(Classes,on_delete=models.CASCADE)