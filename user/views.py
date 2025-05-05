from django.contrib import messages
from django.shortcuts import redirect, render,HttpResponse
from user.models import register,reportcrime,contactus
from administrator.models import news
from datetime import datetime
import smtplib
import random
from email.message import EmailMessage

# Create your views here.
def index(request):
    return render(request,"index.html")

def reportcrimes(request):
    email=request.session.get('email')
    request.session['link']="reportcrime"
    if email:
        if request.method == "POST":
            rcfname = request.POST.get('name')
            rcphone = request.POST.get("phone")
            rcdob = request.POST.get('dob')
            rcemail = email
            rcgender = request.POST.get('gender')    
            rcid = request.FILES.get('id')

            rccategory = request.POST.get('category')
            rcspecify = request.POST.get('specify')
            rcsocial = request.POST.get('place')
            rcincidate = request.POST.get('idate')
            rcincitime = request.POST.get('itime')
            rconetime = request.POST.get('onetime')
            rclostmoney = request.POST.get('moneylost')
            rcstreet = request.POST.get('street')
            rcarea = request.POST.get('area')
            data=request.session.get('data')
            if data:
                rcarea1 = data.get('rcarea1')
            else:
                rcarea1 = rcarea
            rccity = request.POST.get("city")
            rcstate = request.POST.get("state")
            rcdetail = request.POST.get('desc')
            rcweapon = request.POST.get('weapon')

            rcidentity = request.POST.get('sidentity')
            rcdesc = request.POST.get('sdesc')
            rcbank = request.POST.get('sbank')
            rcproof = request.FILES.get('sevidence')
            rcextra = request.POST.get('addinfo')

            if data:
                rcstatus = data.get('rcstatus')
            else:
                rcstatus = ""

            if data:
                rcdept = data.get('rcdept')
            else:
                rcdept = "Police"

            if data:
                email=data.get('rcemail')
                detail=data.get('rcdetail')
                date=data.get('rcincidate')  
                obj=reportcrime.objects.filter(rcemail=email,rcdetail=detail,rcincidate=date)
                if obj:
                    obj.delete()
            submit = reportcrime(rcfname=rcfname,rcphone=rcphone,rcdob=rcdob,rcemail=rcemail,rcgender=rcgender,rcid=rcid,
                                rccategory=rccategory,rcspecify=rcspecify,rcsocial=rcsocial,rcincidate=rcincidate,rcincitime=rcincitime,
                                rconetime=rconetime,rclostmoney=rclostmoney,rcstreet=rcstreet,rcarea=rcarea,rcarea1=rcarea1,rccity=rccity,
                                rcstate=rcstate,rcdetail=rcdetail,rcweapon=rcweapon,rcidentity=rcidentity,rcdesc=rcdesc,
                                rcbank=rcbank,rcproof=rcproof,rcextra=rcextra,rcstatus=rcstatus,rcdept=rcdept)
            submit.save()
            count=reportcrime.objects.all().count()
            for i in range(count):
                nemail = reportcrime.objects.all()[i].rcemail
                if rcemail == nemail:
                    ndetail = reportcrime.objects.all()[i].rcdetail
                    if rcdetail == ndetail:
                        ndate = reportcrime.objects.all()[i].rcincidate
                        ndate=str(ndate)
                        date1 = datetime.strptime(rcincidate, '%Y-%m-%d')
                        date2 = datetime.strptime(ndate, '%Y-%m-%d')
                        if date1 == date2:
                            rcid=reportcrime.objects.all()[i].rcid
                            rcproof=reportcrime.objects.all()[i].rcproof
            data={'rcfname':rcfname,'rcphone':rcphone,'rcdob':rcdob,'rcemail':rcemail,'rcgender':rcgender,
                                'rccategory':rccategory,'rcspecify':rcspecify,'rcsocial':rcsocial,'rcincidate':rcincidate,'rcincitime':rcincitime,
                                'rconetime':rconetime,'rclostmoney':rclostmoney,'rcstreet':rcstreet,'rcarea':rcarea,'rccity':rccity,
                                'rcstate':rcstate,'rcdetail':rcdetail,'rcweapon':rcweapon,'rcidentity':rcidentity,'rcdesc':rcdesc,
                                'rcbank':rcbank,'rcextra':rcextra,'rcarea1':rcarea1,'rcstatus':rcstatus,'rcdept':rcdept}
            request.session['data']=data
            return render(request,"preview.html",data)
        return render(request,"report_crime.html")
    else:
        return render(request,"login.html")

def login(request):
    from django.urls import reverse
    from django.shortcuts import redirect
    if request.method == "POST":
        ch_username = request.POST.get('username')
        ch_password = request.POST.get('password')
        count=register.objects.all().count()
        for i in range(count):
            nusername = register.objects.all()[i].email
            if ch_username == nusername:
                npassword = register.objects.all()[i].passwd
                if npassword == ch_password:
                    if ch_username:
                        request.session['email'] = nusername  # Store the user's ID in the session
                        check=request.session.get('link')
                        if check=="dashboard":
                            return redirect(dashboard)
                        if check=="reportcrime":
                            return render(request, 'report_crime.html')
                        return render(request, 'index.html')
            else:
                flag=1
        if flag==1:
            msg="Username or Password is wrong!"
            return render(request,"login.html",{'msg':msg})
    return render(request,"login.html")

def registers(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get("lname")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        passwd=request.POST.get("password")
        conpw=request.POST.get("confirm-psw")
        city=request.POST.get("city")
        state=request.POST.get("state")
        count=register.objects.all().count()
        for i in range(count):
            nemail=register.objects.all()[i].email
            if nemail == email:
                msg1="Email already exists! Login or enter different emailid."
                return render(request,"register.html",{'msg1':msg1})
        if passwd == conpw:
            submit=register(fname=fname, lname=lname, phone=phone, email=email, passwd=passwd, city=city, state=state)
            submit.save()
            return render(request,"login.html",)

        else:
            msg="Password fields must match!"
            return render(request,"register.html",{'msg':msg})
    return render(request,"register.html",)

def contact_us(request):
    if request.method == "POST":
        cname = request.POST.get('name')
        cemail = request.POST.get('email')
        cmessage = request.POST.get('message')

        data = contactus(cname=cname,cemail=cemail,cmessage=cmessage)
        data.save()
    return render(request,"contact-us.html")

def help(request):
    return render(request,"help.html")

def opennews(request):
    return render(request,"news.html")

def preview(request):
    return render(request,"preview.html")

def back(request):
    data=request.session.get('data')
    return render(request,"report_crime.html",data)

def dashboard(request):
    email=request.session.get('email')
    request.session['link']="dashboard"
    if email:
        count=register.objects.all().count()
        for i in range(count):
            nemail = register.objects.all()[i].email
            if email == nemail:
                nfname = register.objects.all()[i].fname
                nphone = register.objects.all()[i].phone
                nlname = register.objects.all()[i].lname
                ncity = register.objects.all()[i].city
                nstate = register.objects.all()[i].state
                nmail = register.objects.all()[i].email
        count1=reportcrime.objects.all().count()
        ddob = None
        for i in range(count1):
            demail = reportcrime.objects.all()[i].rcemail
            if demail == nmail:
                ddob = reportcrime.objects.all()[i].rcdob
                dgender = reportcrime.objects.all()[i].rcgender
                did = reportcrime.objects.all()[i].rcid
            if ddob:
                details = {
                    'fname': nfname,
                    'lname': nlname,
                    'phone': nphone,
                    'city':ncity,
                    'email':nmail,
                    'state':nstate,
                    'dob':ddob,
                    'gender':dgender,
                    'id':did,
                }
            else:
                details = {
                    'fname': nfname,
                    'lname': nlname,
                    'phone': nphone,
                    'city':ncity,
                    'email':nmail,
                    'state':nstate,
                }
        details1 = reportcrime.objects.all()
        request.session['data']=None
        return render(request,"dashboard.html",{'details':details,'details1':details1})
    return render(request,"login.html")

def forgot(request):
    if request.method == "POST":
        global femail
        femail=request.POST.get('email')
        count=register.objects.all().count()
        for i in range(count+1):
            nemail=register.objects.all()[i].email
            if nemail == femail:
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login("crime.data.analysis.lj@gmail.com","wyat oxwp zrgy pdqd")
                global otp
                otp = str(random.randint(100000, 999999))
                msg = EmailMessage()
                msg.set_content(
                    "Dear User,\n\n"
                    "You recently requested to reset your password for your account with Crime Data Analysis Website.\n\n"
                    "Please use the following One-Time Password (OTP) to complete the password reset process:\n\n"
                    f"OTP: {otp}\n\n"
                    "Please enter this OTP on the password reset page to verify your identity and create a new password. This OTP is valid for a single use and will expire in 15 minutes.\n\n"
                    "If you did not request this password reset, please ignore this email. Your account security is important to us, and no action is required on your part.\n\n"
                    "If you need further assistance or have any questions, feel free to reach out to our support team at crime.data.analysis.nlj@gmail.com\n\n"
                    "Thank you for choosing us.\n\n"
                    "Best regards."
                )
                msg['Subject'] = 'Crime Data Analysis Password Reset OTP'
                msg['From'] = 'crime.data.analysis.lj@gmail.com'
                msg['To'] = femail
                server.send_message(msg)

                return render(request,"reset.html")          
    return render(request,"forgot.html")

def reset(request):
    if request.method == "POST":
        otp_entered = request.POST.get('otp')
        new_password = request.POST.get('password')
        con_password = request.POST.get('cpassword')
        # Verify OTP
        if otp == otp_entered:
            if new_password == con_password:
                count=register.objects.all().count()
                for i in range(count+1):
                    nemail=register.objects.all()[i].email
                    if nemail == femail:
                        nfname = register.objects.all()[i].fname
                        nlname = register.objects.all()[i].lname
                        nphone = register.objects.all()[i].phone
                        ncity = register.objects.all()[i].city
                        nstate = register.objects.all()[i].state
                        obj = register.objects.filter(email=femail)
                        obj.delete()
                        object=register(fname=nfname,lname=nlname,phone=nphone,email=femail,
                                        passwd=new_password,city=ncity,state=nstate)
                        object.save()
                        return render(request,'login.html')  
            else:
                msg1 = "Password fields must match!"
                return render(request, "reset.html",{'msg1':msg1})
        else:
            msg2 = "Invalid OTP!"
            return render(request, "reset.html",{'msg2':msg2})
    return render(request,"reset.html")

def logout(request):
    if request.method=="POST":
        request.session['email'] = None
    return render(request,"index.html")

def update(request):
    email=request.session.get('email')
    count=reportcrime.objects.all().count()
    idate = request.POST.get("idate")
    itime = request.POST.get("itime")
    for i in range(count):
        nemail = reportcrime.objects.all()[i].rcemail
        if email == nemail:
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
                    rccity = reportcrime.objects.all()[i].rccity
                    rcstate = reportcrime.objects.all()[i].rcstate
                    rcdetail = reportcrime.objects.all()[i].rcdetail
                    rcweapon = reportcrime.objects.all()[i].rcweapon
                    rcidentity = reportcrime.objects.all()[i].rcidentity
                    rcdesc = reportcrime.objects.all()[i].rcdesc
                    rcbank = reportcrime.objects.all()[i].rcbank                    
                    rcproof=reportcrime.objects.all()[i].rcproof
                    rcextra = reportcrime.objects.all()[i].rcextra
                    rcarea1 = reportcrime.objects.all()[i].rcarea1
                    rcstatus = reportcrime.objects.all()[i].rcstatus
                    rcdept = reportcrime.objects.all()[i].rcdept
                    rcdob=str(rcdob)
                    rcincidate=str(rcincidate)
                    rcincitime=str(rcincitime)

                    make_readonly = True
                    data={'rcfname':rcfname,'rcphone':rcphone,'rcdob':rcdob,'rcemail':rcemail,'rcgender':rcgender,
                                'rccategory':rccategory,'rcspecify':rcspecify,'rcsocial':rcsocial,'rcincidate':rcincidate,'rcincitime':rcincitime,
                                'rconetime':rconetime,'rclostmoney':rclostmoney,'rcstreet':rcstreet,'rcarea':rcarea,'rccity':rccity,
                                'rcstate':rcstate,'rcdetail':rcdetail,'rcweapon':rcweapon,'rcidentity':rcidentity,'rcdesc':rcdesc,
                                'rcbank':rcbank,'rcextra':rcextra,'rcstatus':rcstatus,'rcarea1':rcarea1,'rcdept':rcdept,'make_readonly':make_readonly}
                    request.session['data']=data
                    return render(request,"report_crime.html",data)
                
def allnews(request):
    return render(request,"allnews.html")

def articles(request):
    content = request.GET.get('content')
    request.session['content']=content
    return redirect(articles2)

def articles2(request):
    content = request.session.get('content')
    value=request.session.get('tempvalue')
    indarticle = news.objects.filter(title=content,category=value)
    return render(request,"article.html",{"indarticle":indarticle})

def urlfornews(request):
    value = request.GET.get('value')
    request.session['tempvalue']=value
    return redirect(urlfornews2)

def urlfornews2(request):
    value=request.session.get('tempvalue')
    articles = news.objects.filter(category=value) 
    return render(request, "allnews.html", {"articles": articles})