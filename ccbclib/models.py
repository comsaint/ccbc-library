from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=128) #name or title of the book
    code = models.CharField(max_length=10, unique=True) #id code of the book. Normally in format cc-dddd
    area = models.CharField(max_length=32) #perhaps we can get this via the first 2 char of the 'code' field?
    ONSHELF = 'OS'
    BORROWED = 'BR'
    RENEWED = 'RN'
    OVERDUE = 'OD'
    RESERVED = 'RS'
    LOST = 'LS'
    BOOK_STATUS_CHOICE=(
                        (ONSHELF,'On-shelf'),
                        (BORROWED,'Borrowed'),
                        (RENEWED,'Renewed'),
                        (OVERDUE,'Overdue'),
                        (RESERVED,'Reserved'),
                        (LOST,'Lost'),
                        )
    status = models.CharField(max_length=2,
                              choices=BOOK_STATUS_CHOICE,
                              default=ONSHELF)
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
    IDLE = 'I'
    BORROWING = 'B'
    OVERDUING = 'D'
    BORROWER_STATUS_CHOICE=(
                            (IDLE,'Idle'),
                            (BORROWING,'Borrowing'),
                            (OVERDUING,'Overduing'),
                            )
    status = models.CharField(max_length=1,
                              choices=BORROWER_STATUS_CHOICE,
                              default=IDLE)
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
    borrow_date = models.DateField(null=False)
    borrow_manager = models.CharField(max_length=32,default='CCBC')
    due_date = models.DateField(null=False)
    renew_date = models.DateField(null=True)
    renew_manager = models.CharField(max_length=32,default='')
    return_date = models.DateField(null=True)
    return_manager = models.CharField(max_length=32,default='')
    
    def __str__(self):
        return self.book