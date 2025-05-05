from email.message import EmailMessage
import smtplib
from django.shortcuts import redirect, render,HttpResponse
from administrator.models import legalauth,news
from user.models import reportcrime
# Create your views here.
def login(request):
    un = request.POST.get("uname")
    passwd = request.POST.get("pass")
    if request.method == "POST":
        if un == "admin":
            if passwd == "admin1234":
                request.session['aemail'] = un  
                check=request.session.get('link')
                if check=="dashboard":
                    data1 = reportcrime.objects.all()
                    return render(request,"adashboard.html",{'data1':data1})
                if check=="addauth":
                    return render(request, 'aaddauthority.html')
                if check=="seeauth":
                    return render(request, 'aseeauthority.html')
                if check=="viewcom":
                    return render(request, 'aviewcom.html')
                if check=="allauth":
                    return render(request, 'aauthorities.html')
                return redirect(dashboard)
            else:
                flag=1
        else:
            flag=1

        if flag==1:
            msg="Username or Password is wrong!"
            return render(request,"alogin.html",{'msg':msg})
    return render(request, "alogin.html")

def dashboard(request):
    aemail=request.session.get('aemail')
    request.session['link']="dashboard"
    if aemail:
        if request.method == "POST":
            email = request.POST.get('hiddenemail')
            newarea1 = request.POST.get('area1')
            newdept = request.POST.get('dept')

            rcfname = rpdata.get("rcfname")
            rcphone = rpdata.get("rcphone")
            rcdob = rpdata.get("rcdob")
            rcemail = rpdata.get("rcemail")
            rcgender = rpdata.get("rcgender")
            rcid = rpdata.get("rcid")
            rccategory = rpdata.get("rccategory")
            rcspecify = rpdata.get("rcspecify")
            rcsocial = rpdata.get("rcsocial")
            rcincidate = rpdata.get("rcincidate")
            rcincitime = rpdata.get("rcincitime")
            rconetime = rpdata.get("rconetime")
            rclostmoney = rpdata.get("rclostmoney")
            rcstreet = rpdata.get("rcstreet")
            rcarea = rpdata.get("rcarea")
            rccity = rpdata.get("rccity")
            rcstate = rpdata.get("rcstate")
            rcdetail = rpdata.get("rcdetail")
            rcweapon = rpdata.get("rcweapon")
            rcidentity = rpdata.get("rcidentity")
            rcdesc = rpdata.get("rcdesc")
            rcbank = rpdata.get("rcbank")                   
            rcproof=rpdata.get("rcproof")
            rcextra = rpdata.get("rcextra")
            rcstatus = rpdata.get("rcstatus")
            obj=reportcrime.objects.filter(rcemail=email,rcdetail=rcdetail,rcincidate=rcincidate)
            if obj:
                obj.delete()
            submit = reportcrime(rcfname=rcfname,rcphone=rcphone,rcdob=rcdob,rcemail=rcemail,rcgender=rcgender,rcid=rcid,
                                    rccategory=rccategory,rcspecify=rcspecify,rcsocial=rcsocial,rcincidate=rcincidate,rcincitime=rcincitime,
                                    rconetime=rconetime,rclostmoney=rclostmoney,rcstreet=rcstreet,rcarea=rcarea,rcarea1=newarea1,rccity=rccity,
                                    rcstate=rcstate,rcdetail=rcdetail,rcweapon=rcweapon,rcidentity=rcidentity,rcdesc=rcdesc,
                                    rcbank=rcbank,rcproof=rcproof,rcextra=rcextra,rcdept=newdept,rcstatus=rcstatus)
            submit.save()
        data_list = ["Completed", "Fake"]
        data1 = reportcrime.objects.filter()
        return render(request, "adashboard.html", {'data1':data1,'data_list':data_list})
    return render(request, "alogin.html")

def addauth(request):
    aemail=request.session.get('aemail')
    request.session['link']="addauth"
    if aemail:
        if request.method == "POST":
            laemail = request.POST.get("mail")
            lapass = request.POST.get("passwd")
            ladept = request.POST.get("dept")
            laarea = request.POST.get("area")
            lacity = request.POST.get("city")
            lastate = request.POST.get("state")
            lapin = request.POST.get("pin")
            count=legalauth.objects.all().count()
            for i in range(count):
                nemail=legalauth.objects.all()[i].email
                if nemail == laemail:
                    msg1="Email already exists! Login or enter different emailid."
                    return render(request,"aaddauthority.html",{'msg1':msg1})
                
            submit = legalauth(email=laemail,passwd=lapass,dept=ladept,area=laarea,city=lacity,state=lastate,pinc=lapin)
            submit.save()
            if submit:
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login("crime.data.analysis.lj@gmail.com","wyat oxwp zrgy pdqd")
                msg = EmailMessage()
                msg.set_content(
                    f"Dear User,\n\n"
                    f"Welcome to Crime Data Analysis! We are pleased to inform you that an account has been created for you as a {ladept} by the website administrator.\n\n"
                    "Your login credentials are as follows:\n\n"
                    f"Username: {laemail}\n"
                    f"Password: {lapass}\n\n"
                    "Please use these credentials to log in to your account on our website.\n\n"
                    "Upon logging in, you will have access to the crime report management, data analysis tools, etc.\n\n"
                    "If you have any questions or encounter any issues while logging in or using our website, please don't hesitate to contact us at crime.data.analysis.lj@gmail.com. We're here to help!\n\n"
                    "Thank you for joining us in our mission to analyze and address crime data effectively.\n\n"
                    "Best regards."
                )
                msg['Subject'] = 'Login Credentials for Crime Data Analysis Website'
                msg['From'] = 'crime.data.analysis.lj@gmail.com'
                msg['To'] = laemail
                server.send_message(msg)
            return redirect(seeauth)
        return render(request,"aaddauthority.html")
    return render(request,"alogin.html")

def seeauth(request):
    aemail=request.session.get('aemail')
    request.session['link']="seeauth"
    if aemail:
        if request.method == "POST":
            hemail = request.POST.get("email")
            count = legalauth.objects.all().count()
            for i in range(count):
                mail = legalauth.objects.all()[i].email
                if hemail==mail:
                    email = legalauth.objects.all()[i].email
                    passwd = legalauth.objects.all()[i].passwd
                    dept = legalauth.objects.all()[i].dept
                    area = legalauth.objects.all()[i].area
                    city = legalauth.objects.all()[i].city
                    state = legalauth.objects.all()[i].state
                    pin = legalauth.objects.all()[i].pinc
                    global data
                    data = {'email':email,'passwd':passwd,'dept':dept,'area':area,'city':city,'state':state,'pin':pin}
                    return render(request,"aseeauthority.html",data)
        data = legalauth.objects.all()
        return render(request,"aauthorities.html",{"data":data})
    return render(request,"alogin.html")

def viewcom(request):
    aemail=request.session.get('aemail')
    request.session['link']="viewcom"
    if aemail:
        if request.method == "POST":
            count = reportcrime.objects.all().count()
            email = request.POST.get("email")
            idate = request.POST.get("date")
            itime = request.POST.get("time")
            for i in range(count):
                nemail = reportcrime.objects.all()[i].rcemail
                if email == nemail:
                    from dateutil import parser
                    ndate = reportcrime.objects.all()[i].rcincidate
                    ntime = reportcrime.objects.all()[i].rcincitime
                    idate=str(idate)
                    ndate=str(ndate)
                    idate = parser.parse(idate)
                    ndate = parser.parse(ndate)
                    if idate == ndate:
                        ntime = reportcrime.objects.all()[i].rcincitime
                        itime=str(itime)
                        ntime=str(ntime)
                        itime = parser.parse(itime)
                        ntime = parser.parse(ntime)
                        if itime == ntime:
                            rcfname = reportcrime.objects.all()[i].rcfname
                            rcphone = reportcrime.objects.all()[i].rcphone
                            rcdob = reportcrime.objects.all()[i].rcdob
                            rcemail = reportcrime.objects.all()[i].rcemail
                            rcgender = reportcrime.objects.all()[i].rcgender
                            rcid = reportcrime.objects.all()[i].rcid
                            rccategory = reportcrime.objects.all()[i].rccategory
                            rcspecify = reportcrime.objects.all()[i].rcspecify
                            rcsocial = reportcrime.objects.all()[i].rcsocial
                            rcincidate = reportcrime.objects.all()[i].rcincidate
                            rcincitime = reportcrime.objects.all()[i].rcincitime
                            rconetime = reportcrime.objects.all()[i].rconetime
                            rclostmoney = reportcrime.objects.all()[i].rclostmoney
                            rcstreet = reportcrime.objects.all()[i].rcstreet
                            rcarea = reportcrime.objects.all()[i].rcarea
                            rcarea1 = reportcrime.objects.all()[i].rcarea1
                            rccity = reportcrime.objects.all()[i].rccity
                            rcstate = reportcrime.objects.all()[i].rcstate
                            rcdetail = reportcrime.objects.all()[i].rcdetail
                            rcweapon = reportcrime.objects.all()[i].rcweapon
                            rcidentity = reportcrime.objects.all()[i].rcidentity
                            rcdesc = reportcrime.objects.all()[i].rcdesc
                            rcbank = reportcrime.objects.all()[i].rcbank                    
                            rcproof=reportcrime.objects.all()[i].rcproof
                            rcextra = reportcrime.objects.all()[i].rcextra
                            rcdept = reportcrime.objects.all()[i].rcdept
                            rcstatus = reportcrime.objects.all()[i].rcstatus
                            rcdob=str(rcdob)
                            rcincidate=str(rcincidate)
                            rcincitime=str(rcincitime)
                            global rpdata
                            rpdata={'rcfname':rcfname,'rcphone':rcphone,'rcdob':rcdob,'rcemail':rcemail,'rcgender':rcgender,'rcid':rcid,
                                        'rccategory':rccategory,'rcspecify':rcspecify,'rcsocial':rcsocial,'rcincidate':rcincidate,'rcincitime':rcincitime,
                                        'rconetime':rconetime,'rclostmoney':rclostmoney,'rcstreet':rcstreet,'rcarea':rcarea,'rcarea1':rcarea1,'rccity':rccity,
                                        'rcstate':rcstate,'rcdetail':rcdetail,'rcweapon':rcweapon,'rcidentity':rcidentity,'rcdesc':rcdesc,
                                        'rcbank':rcbank,'rcproof':rcproof,'rcextra':rcextra,'rcdept':rcdept,'rcstatus':rcstatus}
                            return render(request,"aviewcom.html",rpdata)
        data1 = reportcrime.objects.all()
        return render(request,"adashboard.html",{'data1':data1})         
    return render(request,"alogin.html")  

def allauth(request):
    aemail=request.session.get('aemail')
    request.session['link']="allauth"
    if aemail:
        data = legalauth.objects.all()
        return render(request,"aauthorities.html",{"data":data})
    return render(request,"alogin.html")

def update(request):
    return render(request,"aupdate.html",rpdata)

def fakecom(request):
    aemail=request.session.get('aemail')
    request.session['link']="viewcom"
    if aemail:
        if request.method == "POST":
            count = reportcrime.objects.all().count()
            email = request.POST.get("email")
            idate = request.POST.get("date")
            itime = request.POST.get("time")
            for i in range(count):
                nemail = reportcrime.objects.all()[i].rcemail
                if email == nemail:
                    from dateutil import parser
                    ndate = reportcrime.objects.all()[i].rcincidate
                    ntime = reportcrime.objects.all()[i].rcincitime
                    idate=str(idate)
                    ndate=str(ndate)
                    idate = parser.parse(idate)
                    ndate = parser.parse(ndate)
                    if idate == ndate:
                        ntime = reportcrime.objects.all()[i].rcincitime
                        itime=str(itime)
                        ntime=str(ntime)
                        itime = parser.parse(itime)
                        ntime = parser.parse(ntime)
                        if itime == ntime:
                            rcfname = reportcrime.objects.all()[i].rcfname
                            rcphone = reportcrime.objects.all()[i].rcphone
                            rcdob = reportcrime.objects.all()[i].rcdob
                            rcemail = reportcrime.objects.all()[i].rcemail
                            rcgender = reportcrime.objects.all()[i].rcgender
                            rcid = reportcrime.objects.all()[i].rcid
                            rccategory = reportcrime.objects.all()[i].rccategory
                            rcspecify = reportcrime.objects.all()[i].rcspecify
                            rcsocial = reportcrime.objects.all()[i].rcsocial
                            rcincidate = reportcrime.objects.all()[i].rcincidate
                            rcincitime = reportcrime.objects.all()[i].rcincitime
                            rconetime = reportcrime.objects.all()[i].rconetime
                            rclostmoney = reportcrime.objects.all()[i].rclostmoney
                            rcstreet = reportcrime.objects.all()[i].rcstreet
                            rcarea = reportcrime.objects.all()[i].rcarea
                            rcarea1 = reportcrime.objects.all()[i].rcarea1
                            rccity = reportcrime.objects.all()[i].rccity
                            rcstate = reportcrime.objects.all()[i].rcstate
                            rcdetail = reportcrime.objects.all()[i].rcdetail
                            rcweapon = reportcrime.objects.all()[i].rcweapon
                            rcidentity = reportcrime.objects.all()[i].rcidentity
                            rcdesc = reportcrime.objects.all()[i].rcdesc
                            rcbank = reportcrime.objects.all()[i].rcbank                    
                            rcproof=reportcrime.objects.all()[i].rcproof
                            rcextra = reportcrime.objects.all()[i].rcextra
                            rcdept = reportcrime.objects.all()[i].rcdept
                            rcstatus = reportcrime.objects.all()[i].rcstatus
                            rcdob=str(rcdob)
                            rcincidate=str(rcincidate)
                            rcincitime=str(rcincitime)
                            global rpdata
                            rpdata={'rcfname':rcfname,'rcphone':rcphone,'rcdob':rcdob,'rcemail':rcemail,'rcgender':rcgender,'rcid':rcid,
                                        'rccategory':rccategory,'rcspecify':rcspecify,'rcsocial':rcsocial,'rcincidate':rcincidate,'rcincitime':rcincitime,
                                        'rconetime':rconetime,'rclostmoney':rclostmoney,'rcstreet':rcstreet,'rcarea':rcarea,'rcarea1':rcarea1,'rccity':rccity,
                                        'rcstate':rcstate,'rcdetail':rcdetail,'rcweapon':rcweapon,'rcidentity':rcidentity,'rcdesc':rcdesc,
                                        'rcbank':rcbank,'rcproof':rcproof,'rcextra':rcextra,'rcdept':rcdept,'rcstatus':rcstatus}
                            return render(request,"afakecom.html",rpdata)
        data1 = reportcrime.objects.all()
        return render(request,"adashboard.html",{'data1':data1})         
    return render(request,"alogin.html")  

def addnews(request):
    aemail=request.session.get('aemail')
    if aemail:
        if request.method == "POST":
            title = request.POST.get("title")
            content = request.POST.get("content")
            author = request.POST.get("author")
            pubdate = request.POST.get("pubdate")
            category = request.POST.get("category")
            img1 = request.FILES.get("img1")
            img2 = request.FILES.get("img2")
            img3 = request.FILES.get("img3")
            img4 = request.FILES.get("img4")
            img5 = request.FILES.get("img5")
            source = request.POST.get("source")
            url = request.POST.get("url")
            submit = news(title=title,content=content,author=author,pubdate=pubdate,category=category,img1=img1,img2=img2,
                          img3=img3,img4=img4,img5=img5,source=source,url=url)
            submit.save()
        return render(request,"addnews.html")
    return render(request,"alogin.html")