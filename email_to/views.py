import socket
import smtplib

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import mail

from .forms import SendEmailForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            from_email = form.cleaned_data.get('sender_email')
            recipient_list = [form.cleaned_data.get('receiver_email')]
            cc_myself = form.cleaned_data.get('cc_myself')

            if cc_myself:
                recipient_list.append(from_email)

            try:
                pass
                # mail.send_mail(subject, message, from_email, recipient_list)
            except socket.gaierror:
                # Failed to get address info. of EMAIL_HOST: 'smtp.gmail.com'
                messages.warning(request, 'Unable to get Address Information')
            except smtplib.SMTPConnectError:
                # Unable to connect to connect to smtp server
                messages.warning(request, 'Cannot connect to SMTP server')
            else:
                messages.success(request, 'email sent')
        else:
            messages.error(request, 'email not sent')
    else:
        form = SendEmailForm()

    context = {
        'form': form
    }

    return render(request, 'email_to/index.html', context=context)
