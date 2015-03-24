from django.db import models
#from django.utils import timezone
import datetime
#from datetime import date

from ccbclib.constants import RENEW_DURATION, BORROW_DURATION, BOOK_AREA, BOOK_LANG
from django.db.models.fields import AutoField

# Create your models here.
class Book(models.Model):
    idbook = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128) #name or title of the book
    code = models.CharField(max_length=8) #id code of the book. Normally in format ccdddd
    #area = models.CharField(max_length=32) #perhaps we can get this via the first char of the 'code' field?
    statusflag = models.CharField(max_length=16,choices=(('NM','Normal'),('SP','Special')),default='NM')#this should only be changed in admin view
    
    def get_area(self):
        """
        Get the area of which a book is in via 1st field of the code.
        """
        return BOOK_AREA[self.code[0]]
    
    def get_language(self):
        """
        Get the language of a book via 2nd field of the code.
        """
        return BOOK_LANG[self.code[1]]
        
    def get_book_status(self):
        """
        Get the status of a book.
        """
        if self.statusflag == 'NM': # is the book in normal status (not lost/reserved etc.)
            q = Transaction.objects.filter(book = self,return_date = None) #is this book currently borrowed?
            if q.exists() and q[0].renew_date == None:
                return 'Borrowed'
            elif q.exists() and q[0].renew_date != None:
                return 'Renewed'
            else:
                return 'Onshelf'
        else:
            return 'Reserved'
    get_book_status.short_description = 'Status'
    
    #for statistics
    def get_times_borrowed(self):
        """
        Check how many times this book has been borrowed.
        Note that some books have multiple copies. Here we aggregate all books with same title as one.
        """
        q = Transaction.objects.filter(book__name = self.name)
        return len(q)
    get_times_borrowed.short_description = 'Times Borrowed'
    
    def __str__(self):
        return self.name

class Borrower(models.Model):
    idborrower = AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True,blank=True,default='no_email@no_email.com') #some do not have/use email
    cellgroup = models.CharField(max_length=128)
    statusflag = models.CharField(max_length=16,choices=(('NM','Normal'),('SP','Special')),default='NM')#this should only be changed in admin view
    
    def get_borrower_status(self):
        """
        Get status of a borrower.
        """
        if self.statusflag == 'NM': # is the book in normal status (not lost/reserved etc.)
            q = Transaction.objects.filter(borrower = self,return_date = None).order_by('-borrow_date') #is this user currently borrowing a book?
            if q.exists():
                if q[0].is_overdue():
                    return 'Overdue'
                else:
                    return 'Borrowing'
            else:
                return 'Idle'
        else:
            return 'Reserved'
    get_borrower_status.short_description='Status'
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    idtransaction = AutoField(primary_key=True)
    book = models.ForeignKey('Book',related_name='book')
    borrower = models.ForeignKey('Borrower',related_name='borrower')
    borrow_date = models.DateField()
    borrow_manager = models.CharField(max_length=32,default=None)
    renew_date = models.DateField(null=True,blank=True,default=None)
    renew_manager = models.CharField(max_length=32,null=True,blank=True,default=None)
    return_date = models.DateField(null=True,blank=True,default=None)
    return_manager = models.CharField(max_length=32,null=True,blank=True,default=None)
    
    def cal_due_date(self):
        """
        Returns the due date of a book.
        """
        if self.renew_date!=None:
            return self.renew_date + datetime.timedelta(days=RENEW_DURATION)
        else:
            return self.borrow_date + datetime.timedelta(days=BORROW_DURATION)
    cal_due_date.short_description = 'Due Date'
    
    def is_overdue(self):
        """
        Returns TRUE if the book is overdue.
        """
        return self.cal_due_date() < datetime.date.today()
    is_overdue.boolean = True
    is_overdue.short_description = 'Is it overdue?'
    
    def is_returned(self):
        """
        Check if this book has been returned.
        """
        return self.return_date!=None
    is_returned.boolean = True
    is_returned.short_description = 'Is it returned?'
    
    def __str__(self):
        return ','.join([str(self.idtransaction),self.book.name,self.borrower.name,str(self.borrow_date)])