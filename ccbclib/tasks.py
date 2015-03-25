#from post_office import mail
from django.core.mail import EmailMessage
import os

def print_task():
    print("In a task!")
    
def SendTestMail():
    print('Email in preparation...')
    email=EmailMessage('Subject here', 'Here is the message.', to = ['comsaint26@hotmail.com'])
    print('Email is ready...')
    print(os.environ.get('MY_GMAIL_ADDRESS',''),os.environ.get('MY_GMAIL_PW',''))
    email.send()
    print('Email sent!')
    
def CheckDueSoon():
    pass

def CheckOverDue():
    pass
    
def SendDueEmail():
    pass

def SendOverdueEmail():
    pass