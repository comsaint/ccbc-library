from django.db import models
import datetime
from django.core.urlresolvers import reverse

from ccbclib.constants import RENEW_DURATION, BORROW_DURATION, BOOK_AREA, BOOK_LANG, CODE_COLOUR
from django.db.models.fields import AutoField
#from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    idbook = models.AutoField(primary_key=True)
    
    code_colour = models.CharField(max_length=16,null=True,blank=True,choices=CODE_COLOUR,default=None)
    code_number = models.CharField(max_length=6,default=None,unique=True) #id code of the book. Normally in format ccdddd
    name = models.CharField(max_length=128) #name or title of the book
    quantity = models.IntegerField(default=0)
    publisher = models.CharField(max_length=128,null=True,blank=True,default=None)
    author = models.CharField(max_length=128,null=True,blank=True,default=None)
    lang = models.CharField(max_length=8,choices=BOOK_LANG)
    book_area = models.CharField(max_length=128,choices=BOOK_AREA,default='UNKNOWN')
    
    statusflag = models.CharField(max_length=16,choices=(('NM','Normal'),('SP','Special')),default='NM')#this should only be changed in admin view
        
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
    
    def get_absolute_url(self):
        #return reverse('book-detail', kwargs={'pk':self.pk})
        return reverse('ccbclib:success')
    
    def __str__(self):
        return ' -- '.join([self.name,self.code_number])
    
    class Meta:
        ordering = ["code_number"]


class BorrowerManager(models.Manager):
    def get_queryset(self):
        q = Borrower.objects.all()
        q_ids = [o.idborrower for o in q if o.get_borrower_status()=='Idle']
        q = q.filter(idborrower__in=q_ids)
        return q


class Borrower(models.Model):
    idborrower = AutoField(primary_key=True)
    
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True,blank=True,default=None) #some do not have/use email
    cellgroup = models.CharField(max_length=128)
    statusflag = models.CharField(max_length=16,choices=(('NM','Normal'),('SP','Special')),default='NM')#this should only be changed in admin view
    objects = models.Manager() # The default manager.
    idle_borrowers = BorrowerManager()
    
    def get_borrower_status(self):
        """
        Get status of a borrower.
        """
        if self.statusflag == 'NM': # is the book in normal status (not lost/reserved etc.)
            q = Transaction.objects.filter(borrower = self,return_date = None) #is this user currently borrowing a book?
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
    
    def get_times_overdue(self):
        q = Transaction.overdued_transactions.filter(borrower=self)
        return len(q)
    get_times_overdue.short_description='Times overdue'
    
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('name','phone')
        ordering = ["name"]

class TransactionManager(models.Manager):
    def get_queryset(self):
        q = Transaction.objects.all()
        q_ids = [o.idtransaction for o in q if o.was_overdue()]
        q = q.filter(idtransaction__in=q_ids)
        return q

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
    objects = models.Manager() # The default manager.
    overdued_transactions = TransactionManager()
    
    def cal_due_date(self):
        """
        Returns the due date of a book.
        """
        if self.renew_date!=None:
            return self.renew_date + datetime.timedelta(days=RENEW_DURATION)
        else:
            return self.borrow_date + datetime.timedelta(days=BORROW_DURATION)
    cal_due_date.short_description = 'Due Date'
    
    def is_due_soon(self):
        """
        Go over all UNRETURNED transactions. See if they are to be due in 3 days. 
        """
        #(Not returned AND Not overdue AND due within 3 days)
        return (self.return_date==None) and (self.cal_due_date() >= datetime.date.today()) and (self.cal_due_date() < datetime.date.today()+datetime.timedelta(days=3))
    is_due_soon.boolean = True
    is_due_soon.short_description = 'Will it due soon?'
    
    def is_overdue(self):
        """
        Returns TRUE if the book is overdue (now).
        Past overdue items will return FASLE.
        """
        return (self.return_date==None) and (self.cal_due_date() < datetime.date.today())
    is_overdue.boolean = True
    is_overdue.short_description = 'Is it overdue?'
    
    def was_overdue(self):
        """
        Returns TRUE if the book is/was overdue (for all times).
        Past overdue items will return TRUE.
        """
        if self.return_date==None:
            return self.cal_due_date() < datetime.date.today()
        else:
            return self.cal_due_date() < self.return_date
    was_overdue.boolean = True
    was_overdue.short_description = 'Was it overdue?'
    
    def is_returned(self):
        """
        Check if this book has been returned.
        """
        return self.return_date!=None
    is_returned.boolean = True
    is_returned.short_description = 'Is it returned?'
    
    def __str__(self):
        return ','.join([str(self.idtransaction),self.book.name,self.borrower.name,str(self.borrow_date)])
    
    class Meta:
        ordering = ["-idtransaction"]
