import django_tables2 as tables
from ccbclib.models import Book, Borrower, Transaction

class BookTable(tables.Table):
    idbook = tables.Column(verbose_name="id")
    get_area = tables.Column(verbose_name="Field",orderable=False)
    get_language = tables.Column(verbose_name="Language",orderable=False)
    get_book_status = tables.Column(verbose_name="Status",orderable=False)
    get_times_borrowed = tables.Column(verbose_name="Times borrowed",orderable=False)
    class Meta:
        model = Book
        attrs = {"class": "paleblue"}
        exclude = ("statusflag",)

class BorrowerTable(tables.Table):
    idborrower = tables.Column(verbose_name="id")
    get_borrower_status = tables.Column(verbose_name="Status",orderable=False)
    class Meta:
        model = Borrower
        attrs = {"class": "paleblue"}
        exclude = ("statusflag",)

class TransactionTable(tables.Table):
    idtransaction = tables.Column(verbose_name="id")
    cal_due_date = tables.DateColumn(verbose_name="Due Date",orderable=False)
    is_returned = tables.BooleanColumn(verbose_name="Is it returned?",orderable=False)
    is_overdue = tables.BooleanColumn(verbose_name="Is it overdue?",orderable=False)
    class Meta:
        model = Transaction
        attrs = {"class": "paleblue"}