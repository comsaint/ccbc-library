"""
Populate sample data to fill in the database.
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccbc_library.settings')

import django
django.setup()

from ccbclib.models import Book, Borrower, Transaction
from ccbclib.constants import BOOK_STATUS_CHOICE, BORROWER_STATUS_CHOICE
import datetime
from datetime import date

def populate():
    #add books
    book_1 = add_book('Why in Jesus', 'AA0001', 'WY', 'OS', 1, 0)
    book_2 = add_book('What in Jesus', 'AS0002', 'AT', 'BR', 18, 1)
    book_3 = add_book('Where is Jesus', 'HR0003', 'ER', 'OD', 4, 1)
    
    #add borrowers
    alice = add_borrower('Alice Ain', '0413245666', 'alice@example.com', 'K&J', 'I', 4, 0)
    bob = add_borrower('Bob Bod', '0413999454', 'bob@gmail.com', 'Q&A', 'Ball', 2, 1)
    cathy = add_borrower('Cathy Chan', '0416345176', 'cathy@hotmail.com', 'D&C', 'D', 1, 1)
    
    #add transactions
    add_transaction(book_1, bob, date.today(), 'LP', '', 'LP', datetime.date.today()-datetime.timedelta(days=11), 'ZY')
    add_transaction(book_2, alice, date.today()-datetime.timedelta(days=13), 'ZY', date.today()-datetime.timedelta(days=1), 'LP', '', '')
    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_book(name, code, area, status, tb, td):
    p = Book.objects.get_or_create(name=name,code=code,area=area,status=status,times_borrowed=tb,times_overdue=td)
    p.save()
    return p

def add_borrower(name,phone,email,cellgroup,status,borrow_count,overdue_count):
    p = Borrower.objects.get_or_create(name=name,phone=phone,email=email,cellgroup=cellgroup,status=status,borrow_count=borrow_count,overdue_count=overdue_count)
    p.save()
    return p

def add_transaction(book,borrower,borrow_date,borrow_manager,renew_date,renew_manager,return_date,return_manager):
    p = Transaction.objects.get_or_create(book=book,borrower=borrower,borrow_date=borrow_date,borrow_manager=borrow_manager,renew_date=renew_date,renew_manager=renew_manager,return_date=return_date,return_manager=return_manager)
    p.save()
    return p

def set_book_fields(book_id, fieldname,value):
    f = Book.objects.get(id=book_id)
    f.fieldname = value
    f.save()
    
# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()
    print("Done population.")