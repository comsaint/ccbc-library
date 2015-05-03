"""
Populate sample data to fill in the database.
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccbc_library.deploy_settings')

import django
django.setup()

from ccbclib.models import Book, Borrower, Transaction
import csv

def populate():
    #add books
    #book_1 = add_book('I am book 1', 'AC0001')
    #book_2 = add_book('I am book 2', 'BC0002')
    #book_3 = add_book('I am book 3', 'AE0003')
    
    #Read csv of library record
    with open('Capel-lib-record-updated-20141218-updated.csv', 'r') as f:
        reader = csv.reader(f)
        rownum=0
        for row in reader:
            if rownum == 0:
                headers = row #not used
                print(headers)
    #####################################################################
    ########### Here we assume the following headers in file:############
    
    # COLUMN[0] : 'Code Colour'    => code_colour
    # COLUMN[1] : 'Code number'    => code_number
    # COLUMN[2] : 'Names'          => name
    # COLUMN[3] : 'Qty'            => quantity
    # COLUMN[4] : 'Publisher'      => publisher
    # COLUMN[5] : 'Author'         => author
    # COLUMN[6] : 'Language'       => lang
    # COLUMN[7] : '類別'            => book_area
    
    # Double check this before adding books into database.
    #####################################################################
            elif row[2] != '': #Must have a name
                add_book(name=row[2], code_number=row[1],code_colour=row[0],quantity=row[3],publisher=row[4],author=row[5],lang=row[6],book_area=row[7])
            else:
                pass
            
            rownum += 1
            print(rownum)
    f.close()
    
    
    #add borrowers
    #alice = add_borrower('Alice Ain', '1234567890', 'alice@example.com', 'K&J cell') #no statusflag
    #bob = add_borrower('Bob Buddy', '0413999454', 'bob@gmail.com', 'Q&A cell') 
    #cathy = add_borrower('Cathy Chan', '0416345176', 'cathy@hotmail.com', 'D&C cell')
    
    #add transactions
    #add_transaction(book=book_1, borrower=bob, borrow_date=date.today(), borrow_manager='LP',return_date=datetime.date.today()-datetime.timedelta(days=11), return_manager='ZY')
    #add_transaction(book=book_2, borrower=alice, borrow_date=date.today()-datetime.timedelta(days=13), borrow_manager='ZY', renew_date=date.today()-datetime.timedelta(days=1), renew_manager='LP')
    #add_transaction(book=book_3, borrower=cathy, borrow_date=date.today()-datetime.timedelta(days=15), borrow_manager='Abby')

def add_book(name, code_number,code_colour,quantity,publisher,author,lang,book_area,statusflag='NM'):
    p = Book.objects.get_or_create(name=name,code_number=code_number,code_colour=code_colour,quantity=quantity,publisher=publisher,author=author,lang=lang,book_area=book_area,statusflag=statusflag)[0]
    p.save()
    return p

def add_borrower(name,phone,email,cellgroup):
    p = Borrower.objects.get_or_create(name=name,phone=phone,email=email,cellgroup=cellgroup)[0]
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
    #print("Starting population script...")
    populate()
    # try to add a borrower
    alice = add_borrower('Alice Ain', '1234567890', 'alice@example.com', 'TEST cell')
    #print("Done population.")