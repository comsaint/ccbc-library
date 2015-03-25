import django_tables2 as tables
from ccbclib.models import Book, Borrower, Transaction

class BookTable(tables.Table):
    idbook = tables.Column(verbose_name="id")
    get_area = tables.Column(verbose_name="Field")
    get_language = tables.Column(verbose_name="Language")
    get_book_status = tables.Column(verbose_name="Status")
    get_times_borrowed = tables.Column(verbose_name="Times borrowed")
    class Meta:
        model = Book
        attrs = {"class": "paleblue"}

class BorrowerTable(tables.Table):
    idborrower = tables.Column(verbose_name="id")
    get_borrower_status = tables.Column(verbose_name="Status")
    class Meta:
        model = Borrower
        attrs = {"class": "paleblue"}

class TransactionTable(tables.Table):
    idtransaction = tables.Column(verbose_name="id")
    is_returned = tables.BooleanColumn(verbose_name="Is it returned?")
    is_overdue = tables.BooleanColumn(verbose_name="Is/Was it overdue?")
    class Meta:
        model = Transaction
        attrs = {"class": "paleblue"}
        #sequence = ()