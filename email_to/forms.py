from django import forms
# from mailsend.settings import EMAIL_HOST_USER
from django.conf import settings            # better way to access settings


class SendEmailForm(forms.Form):
    sender_email = forms.EmailField(initial=settings.EMAIL_HOST_USER,
                                    label="Sender",
                                    disabled=True,
                                    )
    receiver_email = forms.EmailField(label="Receiver",
                                      error_messages={
                                          'required': "Who are you emailing to?",
                                          'invalid': "Invalid Email Address, "
                                                     "Refer to the information on the Place Holder"
                                      })
    subject = forms.CharField(required=False, max_length=100)
    message = forms.CharField(help_text='Your can write anything you want ...',
                              widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)

    sender_email.widget.attrs.update({'class': 'form-control form-control-sm'})
    receiver_email.widget.attrs.update({'class': 'form-control form-control-sm', 'placeholder': 'example@gmail.com'})
    subject.widget.attrs.update({'class': 'form-control form-control-sm', 'autocomplete': 'off'})
    message.widget.attrs.update({'class': 'form-control form-control-sm', 'rows': 5})
    cc_myself.widget.attrs.update({'class': 'form-check-input'})
