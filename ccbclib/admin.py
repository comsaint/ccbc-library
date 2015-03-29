from django.contrib import admin
from ccbclib.models import Book, Borrower, Transaction

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    fields = ['name','code']
    list_display = ('name','code','get_area','get_language','get_book_status','get_times_borrowed','statusflag',)
    search_fields = ['name']

class BorrowerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','cellgroup']}),
        ('Contact Details',  {'fields': ['phone','email']}),
        ('Status',           {'fields': ['statusflag']}),
    ]
    list_display = ('name','phone','email','cellgroup','get_borrower_status','get_times_overdue','statusflag')
    
class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['book','borrower']}),
        ('Borrow Details',   {'fields': ['borrow_date','borrow_manager']}),
        ('Renew Details',    {'fields': ['renew_date','renew_manager']}),
        ('Return Details',   {'fields': ['return_date','return_manager']}),
    ]
    list_display = ('idtransaction','book','borrower','borrow_date','renew_date','return_date','borrow_manager','renew_manager','return_manager','cal_due_date','is_returned','is_due_soon','is_overdue','was_overdue')

admin.site.register(Book, BookAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Transaction,TransactionAdmin)