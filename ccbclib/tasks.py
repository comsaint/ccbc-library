#from post_office import mail
from django.core import mail
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
import os
from ccbclib.models import Transaction
import datetime
from django.template.loader import get_template
from django.template import Context
#from django.core.mail import send_mail

def print_task():
    print("In a task!")
    
def SendTestMail():
    print('Email in preparation...')
    email=EmailMessage('Regular Reminder from CCBC', 'A test message is compiled and sent successfully.', 'longpun88@gmail.com', to = ['comsaint26@hotmail.com'])
    print('Email is ready...')
    email.send(fail_silently=False)
    #send_mail('test email', 'hello world', 'longpun88@gmail.com', ['comsaint26@hotmail.com'], fail_silently=False)
    print('Email sent!')

def SendNoticeEmail():
    """
    Check for overdue and due soon books, and send notice e-mails accordingly.
    """
    q = Transaction.objects.filter(return_date=None)
    connection = mail.get_connection()
    connection.open()
    #SendTestMail()
    
    send_cnt = 0
    item_to_send_notice = 0
    sms_sent = 0
    for tran in q:
        if tran.is_overdue() or tran.is_due_soon():
            item_to_send_notice+=1
            if tran.borrower.email:
                print(tran.borrower.email)
                #print('Generate an email...')
                email = EmailGen(tran)
                #print('Email generated successfully. Sending...')
                email.send(fail_silently=False)
                #print('Email sent.')
                send_cnt+=1
                #SMS?
                
    #Also sent a summary email to admin
    summary_email = SummaryEmailGen(datetime.datetime.today().strftime("%c"), item_to_send_notice, send_cnt, sms_sent)
    summary_email.send()
    print('Summary email sent.')
    
    connection.close() # manually close the connection
    print(item_to_send_notice,'items overdue or due soon, with',send_cnt, 'emails sent on', datetime.datetime.today().strftime("%c"),'\n')
    
def EmailGen(tran):
    """
    Returns an EmailMessage object for a particular transaction.
    """
    borrower_name = tran.borrower.name
    book_title = tran.book.name
    due_date = str(tran.cal_due_date())
    from_email = os.environ.get('MY_GMAIL_ADDRESS','')
    to = tran.borrower.email
    
    #Prepare context of email
    if tran.is_overdue():
        subject='CCBC Library - Notice of overdue book'
        plaintext = get_template('ccbclib/email_overdue.txt')
        htmly     = get_template('ccbclib/email_overdue.html')
    else:
        subject='CCBC Library - Notice of book to be due'
        plaintext = get_template('ccbclib/email_duesoon.txt')
        htmly     = get_template('ccbclib/email_duesoon.html')
        
    context_dict = Context({
                            'name':borrower_name,
                            'title':book_title,
                            'due_date':due_date
                            })
    
    text_content = plaintext.render(context_dict)
    html_content = htmly.render(context_dict)
    
    email = EmailMultiAlternatives(subject, text_content, from_email, [to])
    email.attach_alternative(html_content, "text/html")
    return email

def SummaryEmailGen(time,item_notice,email_sent,sms_sent):
    """
    Returns an EmailMessage object which summarizes the records.
    """
    from_email = os.environ.get('MY_GMAIL_ADDRESS','')
    to = from_email
    
    #Prepare context of email
    subject='CCBC Library - Summary of transaction check'
    plaintext = get_template('ccbclib/email_summary.txt')
    htmly     = get_template('ccbclib/email_summary.html')
        
    context_dict = Context({
                            'time':time,
                            'item_notice':item_notice,
                            'email_sent':email_sent,
                            'sms_sent':sms_sent,
                            })
    
    text_content = plaintext.render(context_dict)
    html_content = htmly.render(context_dict)
    
    email = EmailMultiAlternatives(subject, text_content, from_email, [to])
    email.attach_alternative(html_content, "text/html")
    return email