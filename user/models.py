from django.db import models

class register(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    passwd = models.CharField(max_length=16)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    def __str__(self):
        return self.email

class reportcrime(models.Model):
    #Personal Info
    rcfname = models.CharField(max_length=50)
    rcphone = models.IntegerField()
    rcdob = models.DateField()
    rcemail = models.EmailField()
    rcgender = models.CharField(max_length=10)
    rcid = models.FileField(null = True, blank = True, upload_to="Media/",default="")
    def __str__(self):
        return self.rcemail

    #Incident Info
    rccategory = models.CharField(max_length=50)
    rcspecify = models.CharField(max_length=50,default="")
    rcsocial = models.CharField(max_length=50)
    rcincidate = models.DateField()
    rcincitime = models.TimeField()
    rconetime = models.CharField(max_length=10)
    rclostmoney = models.CharField(max_length=10)
    rcstreet = models.CharField(max_length = 30)
    rcarea = models.CharField(max_length=20)
    rcarea1 = models.CharField(max_length=20,default="")
    rccity = models.CharField(max_length=20)
    rcstate = models.CharField(max_length=20)
    rcdetail = models.CharField(max_length=500)
    rcweapon = models.CharField(max_length=10)
    
    rcdept = models.CharField(max_length=50,default="")
    rcstatus = models.CharField(max_length=200,default="")

    #Suspect Info
    rcidentity = models.CharField(max_length=10)
    rcdesc = models.CharField(max_length=500,default="")
    rcbank = models.CharField(max_length=50,default="")
    rcproof = models.FileField(null = True, blank = True, upload_to="Media/",default="")
    rcextra = models.CharField(max_length=500,default="")

class contactus(models.Model):
    cname = models.CharField(max_length=50)
    cemail = models.EmailField()
    cmessage = models.CharField(max_length=600)
    def __str__(self):
        return self.cemail