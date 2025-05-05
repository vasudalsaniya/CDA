from email.message import EmailMessage
import smtplib
from django.shortcuts import redirect, render
from administrator.models import legalauth
from user.models import reportcrime

# Create your views here.
def login(request):
    if request.method == "POST":
        ch_username = request.POST.get('uname')
        ch_password = request.POST.get('pass')
        count = legalauth.objects.all().count()
        for i in range(count):
            nusername = legalauth.objects.all()[i].email
            if ch_username == nusername:
                npassword = legalauth.objects.all()[i].passwd
                if npassword == ch_password:
                    if ch_username:
                        request.session['laemail'] = nusername  
                        return redirect(ladashboard)
            else:
                flag=1
        if flag==1:
            msg="Username or Password is wrong!"
            return render(request,"lalogin.html",{'msg':msg})
    return render(request,"lalogin.html")

def ladashboard(request):
    laemail=request.session.get('laemail')
    if laemail:
        count = legalauth.objects.all().count()
        for i in range(count):
            mail = legalauth.objects.all()[i].email
            if laemail==mail:  
                dept = legalauth.objects.all()[i].dept
                laarea = legalauth.objects.all()[i].area
        data_list = ["Completed", "Fake"]
        data1 = reportcrime.objects.filter(rcarea1=laarea,rcdept=dept)
        return render(request, "ladashboard.html", {'data1':data1,'data_list':data_list})
    return render(request,"lalogin.html")

def update(request):
    laemail=request.session.get('laemail')
    if laemail:
        if request.method == "POST":
            count=reportcrime.objects.all().count()
            status = request.POST.get("status")
            hemail = request.POST.get("hiddenemail")
            idate = request.POST.get("idate")
            itime = request.POST.get("itime")
            for i in range(count):
                nemail = reportcrime.objects.all()[i].rcemail
                if hemail == nemail:
                    from dateutil import parser
                    ndate = reportcrime.objects.all()[i].rcincidate
                    ntime = reportcrime.objects.all()[i].rcincitime
                    ndate = reportcrime.objects.all()[i].rcincidate
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
                            rcdob=str(rcdob)
                            rcincidate=str(rcincidate)
                            rcincitime=str(rcincitime)
                            rcdept = reportcrime.objects.all()[i].rcdept

                            obj=reportcrime.objects.filter(rcemail=rcemail,rcdetail=rcdetail,rcincidate=rcincidate)
                            if obj:
                                obj.delete()
                            submit = reportcrime(rcfname=rcfname,rcphone=rcphone,rcdob=rcdob,rcemail=rcemail,rcgender=rcgender,rcid=rcid,
                                rccategory=rccategory,rcspecify=rcspecify,rcsocial=rcsocial,rcincidate=rcincidate,rcincitime=rcincitime,
                                rconetime=rconetime,rclostmoney=rclostmoney,rcstreet=rcstreet,rcarea=rcarea,rcarea1=rcarea1,rccity=rccity,
                                rcstate=rcstate,rcdetail=rcdetail,rcweapon=rcweapon,rcidentity=rcidentity,rcdesc=rcdesc,
                                rcbank=rcbank,rcproof=rcproof,rcextra=rcextra,rcstatus=status,rcdept=rcdept)
                            submit.save()
                            if submit:
                                server=smtplib.SMTP("smtp.gmail.com",587)
                                server.starttls()
                                server.login("crime.data.analysis.lj@gmail.com","wyat oxwp zrgy pdqd")
                                msg = EmailMessage()
                                msg.set_content(
                                    f"Dear {rcfname},\n\n"
                                    "We hope this email finds you well. We are writing to inform you about a recent update regarding the crime report you filed with Crime Data Analysis.\n\n"
                                    f"Date Reported: {rcincidate}\n"
                                    f"Status: {status}\n\n"
                                    "We understand the importance of staying informed about the status of your report. Rest assured, our team is dedicated to ensuring transparency and accountability throughout the process.\n\n"
                                    "If you have any questions or require further assistance, please do not hesitate to reach out to us at crime.data.analysis.lj@gmail.com. Your feedback and cooperation are highly valued.\n\n"
                                    "Thank you for your cooperation and understanding.\n\n"
                                    "Best regards."
                                )
                                msg['Subject'] = 'Report Status Update Notification'
                                msg['From'] = 'crime.data.analysis.lj@gmail.com'
                                msg['To'] = rcemail
                                server.send_message(msg)
            return redirect(ladashboard)    
        
def details(request):
    laemail=request.session.get('laemail')
    if laemail:
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
                            return render(request,"lacrimedetails.html",rpdata)
        data1 = reportcrime.objects.all()
        return render(request,"ladashboard.html",{'data1':data1})         
    return render(request,"alogin.html")  

def profile(request):
    laemail=request.session.get('laemail')
    if laemail:
        count = legalauth.objects.all().count()
        for i in range(count):
            mail = legalauth.objects.all()[i].email
            if laemail==mail:
                email = legalauth.objects.all()[i].email
                passwd = legalauth.objects.all()[i].passwd
                dept = legalauth.objects.all()[i].dept
                area = legalauth.objects.all()[i].area
                city = legalauth.objects.all()[i].city
                state = legalauth.objects.all()[i].state
                pin = legalauth.objects.all()[i].pinc
                data = {'email':email,'passwd':passwd,'dept':dept,'area':area,'city':city,'state':state,'pin':pin}
                return render(request,"laprofile.html",data)
    return render(request,"lalogin.html")

def statusupdate(request):                                
    return render(request,"lastatusupdate.html",rpdata)

def logout(request):
    if request.method=="POST":
        request.session['laemail'] = None
    return render(request,"lalogin.html")

def fakecom(request):
    laemail=request.session.get('laemail')
    if laemail:
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
                            return render(request,"lafakecom.html",rpdata)
        data1 = reportcrime.objects.all()
        return render(request,"ladashboard.html",{'data1':data1})         
    return render(request,"alogin.html")  