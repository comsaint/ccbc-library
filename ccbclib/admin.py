from django.contrib import admin
from ccbclib.models import Book, Borrower, Transaction
import autocomplete_light

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    fields = ['name','code_number','quantity','publisher','author','book_area','lang',]
    list_display = ('name','code_number','quantity','publisher','author','book_area','lang','get_book_status','get_times_borrowed','statusflag',)
    search_fields = ['code_number']
    #form = autocomplete_light.modelform_factory(Book)

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