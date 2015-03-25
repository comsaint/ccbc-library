from django.contrib import admin
from ccbclib.models import Book, Borrower, Transaction

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    fields = ['name','code']
    list_display = ('name','code','statusflag','get_book_status')
    search_fields = ['name']

class BorrowerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','cellgroup']}),
        ('Contact Details',  {'fields': ['phone','email']}),
        ('Status',           {'fields': ['statusflag']}),
    ]
    list_display = ('name','cellgroup','phone','email','statusflag','get_borrower_status')
    
class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['book','borrower']}),
        ('Borrow Details',   {'fields': ['borrow_date','borrow_manager']}),
        ('Renew Details',    {'fields': ['renew_date','renew_manager']}),
        ('Return Details',   {'fields': ['return_date','return_manager']}),
    ]
    list_display = ('idtransaction','book','borrower','borrow_date','renew_date','return_date','borrow_manager','renew_manager','return_manager','cal_due_date','is_returned','is_overdue')
    #list_filter = ['borrow_date']

admin.site.register(Book, BookAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Transaction,TransactionAdmin)