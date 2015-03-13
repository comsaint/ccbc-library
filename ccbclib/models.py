from django.db import models
from django.utils import timezone
import datetime
from datetime import date

from ccbclib.constants import RENEW_DURATION, BORROW_DURATION, BOOK_STATUS_CHOICE, BORROWER_STATUS_CHOICE

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=128) #name or title of the book
    code = models.CharField(max_length=10, unique=True) #id code of the book. Normally in format ccdddd
    area = models.CharField(max_length=32) #perhaps we can get this via the first 2 char of the 'code' field?
    status = models.CharField(max_length=2,
                              choices=BOOK_STATUS_CHOICE,
                              default='OS')
    times_borrowed = models.PositiveIntegerField(default=0)
    times_overdued = models.PositiveIntegerField(default=0)
    
    def is_overdued(self):
        """
        Check if a book is borrowed.
        """
        return self.status in (self.OVERDUED)
    
    def __str__(self):
        return self.name
"""
class BookRecord(models.Model):
    book_id = models.ForeignKey('Book',related_name='records')
    borrowed_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    returned_date = models.DateField(null=True)
    times_borrowed = models.PositiveIntegerField(default=0)
    times_overdued = models.PositiveIntegerField(default=0)
"""

class Borrower(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True) #some do not have/use email
    cellgroup = models.CharField(max_length=128)
    status = models.CharField(max_length=1,
                              choices=BORROWER_STATUS_CHOICE,
                              default='I')
    borrow_count = models.PositiveIntegerField(default=0)
    overdue_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
"""  
class BorrowerRecord(models.Model):
    borrower = models.ForeignKey('Borrower',related_name='records') 
    borrow_book_name = models.CharField(max_length = 128, null=False)
    borrow_book_date = models.DateField(null=False)
    return_book_date = models.DateField(null=True)
    
    def __str__(self):
        return self.borrower
"""

class Transaction(models.Model):
    book = models.ForeignKey('Book')
    borrower = models.ForeignKey('Borrower')
    borrow_date = models.DateField(auto_now_add=True)
    borrow_manager = models.CharField(max_length=32,default='')
    #due_date = models.DateField(null=False)
    renew_date = models.DateField(null=True)
    renew_manager = models.CharField(max_length=32,default='')
    return_date = models.DateField(null=True)
    return_manager = models.CharField(max_length=32,default='')
    
    def cal_due_date(self):
    # Returns the due date of a book.
        if self.renew_date:
            return self.renew_date + datetime.timedelta(days=RENEW_DURATION)
        else:
            return self.borrow_date + datetime.timedelta(days=BORROW_DURATION)
        
    def is_overdue(self):
    # Returns TRUE if the book is overdue.
        return self.cal_due_date() < datetime.date.today()
    
    def __str__(self):
        return self.book