from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from ccbclib.models import Book,Borrower,Transaction
import datetime
#import registration
#from django.contrib.auth.models import User

#Operations on Transaction model
class BorrowForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.none())
    borrower = forms.ModelChoiceField(queryset=Borrower.objects.none())
    borrow_date = forms.DateField(required=True,initial=datetime.date.today(),help_text='Borrow date',widget=SelectDateWidget())
    #borrow_manager = forms.CharField(required=True,help_text="Manager's Initials")#change this to ChoiceField later
    
    def __init__(self,*args,**kwargs):
        super(BorrowForm,self).__init__(*args,**kwargs)
        self.fields['book'] = forms.ModelChoiceField(queryset=Book.onshelf_books.all(),to_field_name="name",required=True,help_text='Book title')
        self.fields['borrower'] = forms.ModelChoiceField(queryset=Borrower.idle_borrowers.all(), to_field_name="name",required=True,help_text="Borrower's name")
        
    class Meta:
        model = Transaction
        fields = ('book','borrower','borrow_date')
        #exclude =('idtransaction','renew_date','renew_manager','return_date','return_manager',)

class RenewForm(forms.ModelForm):
    idtransaction = forms.ModelChoiceField(queryset=Transaction.objects.none())
    renew_date = forms.DateField(required=True,initial=datetime.date.today(),widget=SelectDateWidget(),help_text='Renew Date')
    #renew_manager = forms.CharField(required=True,help_text="Manager's Initials")#change this to ChoiceField later
    
    def __init__(self,*args,**kwargs):
        super(RenewForm,self).__init__(*args,**kwargs)
        self.fields['idtransaction'] = forms.ModelChoiceField(queryset = Transaction.objects.filter(renew_date__isnull = True, return_date__isnull = True),help_text='Transaction')
        
    class Meta:
        model = Transaction
        fields = ('idtransaction','renew_date',)
        #exclude = ('book','borrower','borrow_date','borrow_manager','return_date','return_manager',)
        
class ReturnForm(forms.ModelForm):
    idtransaction = forms.ModelChoiceField(queryset = Transaction.objects.none())
    return_date = forms.DateField(required=True,initial=datetime.date.today(),widget=SelectDateWidget(),help_text='Return Date')
    #return_manager = forms.CharField(required=True,help_text="Manager's Initials")#change this to ChoiceField later
    
    def __init__(self,*args,**kwargs):
        super(ReturnForm,self).__init__(*args,**kwargs)
        self.fields['idtransaction'] = forms.ModelChoiceField(queryset = Transaction.objects.filter(return_date__isnull = True),help_text='Transaction')
    
    class Meta:
        model = Transaction
        fields = ('idtransaction','return_date',)
        #exclude = ('book','borrower','borrow_date','borrow_manager','renew_date','renew_manager',)

# Operations on Book model
"""
class BookForm(forms.Form):
    name = forms.CharField()
    code = forms.CharField()
"""
        