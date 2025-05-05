from django.db import models

# Create your models here.
class legalauth(models.Model):
    email = models.EmailField()
    passwd = models.CharField(max_length=16)
    dept = models.CharField(max_length=50)
    area = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pinc = models.IntegerField()
    def __str__(self):
        return self.dept
    
class news(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    author = models.CharField(max_length=100)
    pubdate = models.DateField()
    category = models.CharField(max_length=50)
    img1 = models.ImageField(null = True, blank = True, upload_to="Media/")
    img2 = models.ImageField(null = True, blank = True, upload_to="Media/",default="")
    img3 = models.ImageField(null = True, blank = True, upload_to="Media/",default="")
    img4 = models.ImageField(null = True, blank = True, upload_to="Media/",default="")
    img5 = models.ImageField(null = True, blank = True, upload_to="Media/",default="")
    source = models.CharField(max_length=50,default="")
    url = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.category