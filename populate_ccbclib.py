"""
Populate sample data to fill in the database.
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccbc_library.settings')

import django
django.setup()

from ccbclib.models import Book, Borrower, Transaction
#from ccbclib.constants import BOOK_STATUS_CHOICE, BORROWER_STATUS_CHOICE
import datetime
from datetime import date

def populate():
    #add books
    book_1 = add_book('Why in Jesus', 'AA0001', 'WY', 'OS')
    book_2 = add_book('What in Jesus', 'AS0002', 'AT', 'BR')
    book_3 = add_book('Where is Jesus', 'HR0003', 'ER', 'OD')
    
    #add borrowers
    alice = add_borrower('Alice Ain', '0413245666', 'alice@example.com', 'K&J', 'I')
    bob = add_borrower('Bob Buddy', '0413999454', 'bob@gmail.com', 'Q&A') #no status
    cathy = add_borrower('Cathy Chan', '0416345176', 'cathy@hotmail.com', 'D&C', 'D')
    
    #add transactions
    add_transaction(book=book_1, borrower=bob, borrow_date=date.today(), borrow_manager='LP',return_date=datetime.date.today()-datetime.timedelta(days=11), return_manager='ZY')
    add_transaction(book=book_2, borrower=alice, borrow_date=date.today()-datetime.timedelta(days=13), borrow_manager='ZY', renew_date=date.today()-datetime.timedelta(days=1), renew_manager='LP')
    add_transaction(book=book_3, borrower=cathy, borrow_date=date.today()-datetime.timedelta(days=15), borrow_manager='Abby')

def add_book(name, code, area, status):
    p = Book.objects.get_or_create(name=name,code=code,area=area,status=status)[0]
    p.save()
    return p

def add_borrower(name,phone,email,cellgroup,status='I'):
    p = Borrower.objects.get_or_create(name=name,phone=phone,email=email,cellgroup=cellgroup,status=status)[0]
    p.save()
    return p

def add_transaction(book,borrower,borrow_date,borrow_manager,renew_date=None,renew_manager=None,return_date=None,return_manager=None):
    #if (renew_date and renew_manager):
    p = Transaction.objects.get_or_create(book=book,borrower=borrower,borrow_date=borrow_date,borrow_manager=borrow_manager,renew_date=renew_date,renew_manager=renew_manager,return_date=return_date,return_manager=return_manager)[0]
    #else:
    #    p = Transaction.objects.get_or_create(book=book,borrower=borrower,borrow_date=borrow_date,borrow_manager=borrow_manager,renew_date=None,renew_manager=None,return_date=return_date,return_manager=return_manager)[0]
    p.save()
    return p

def set_book_fields(book_id, fieldname,value):
    f = Book.objects.get(id=book_id)
    f.fieldname = value
    f.save()
    
# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()
    print("Done population.")