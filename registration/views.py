from django.shortcuts import render,HttpResponse, render_to_response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.db.models import Q
from .models import HubreeUser,Hubree
from .serializers import HubreeUserSerializer,HubreeSerializer
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def create(request):
    if request.method == 'GET':
        hubree = Hubree.objects.all()
        serializer = HubreeSerializer(hubree,  many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if len(request.POST.get('name'))>=4:   
            email_id=request.POST.get('email')
            hubree=Hubree.objects.filter(email=email_id)
            if hubree:
                return HttpResponse("with this email hubree user is already exist")
            else:
                serializer = HubreeSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    generate_email(email_id)
                    return render(request,'signup-verification.html')
        else:
            return render(request,'sign-up.html', {'data':"Minimum 4 characters"})
def resend(request):
    return render(request, 'resend-email.html')



@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def accounts(request):
    return render(request,'index.html')



def generate_email(email):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    text = "Welcome to Hubree,Welcome to hubree. click below link to activate.\nHere is the link:\nhttp://127.0.0.1:8000.active.views.activate_user"
    html = """\
    <html>
        <head></head>
        <body>

            <h4>Welcome to Hubree,Welcome to hubree. click below link to activate.</h4><br>
            Here is the <a href="http://127.0.0.1:8000.active.views.activate_user">link</a> .
        
        </body>
    </html>
    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.starttls()
    mailserver.login('anuradha@ideathrusts.com','lasyasri')
    mailserver.sendmail("anuradha@ideathrusts.com",email, msg.as_string())
    mailserver.quit()
    return HttpResponse("mail send")


