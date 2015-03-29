from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from ccbclib.models import Book,Borrower,Transaction
import datetime

class BorrowForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.onshelf_books.all(),to_field_name="name",empty_label=None,required=True,help_text='Book title')
    borrower = forms.ModelChoiceField(queryset=Borrower.idle_borrowers.all(), to_field_name="name",empty_label=None,required=True,help_text="Borrower's name") #need to filter out currently borrowing ones...
    borrow_date = forms.DateField(required=True,initial=datetime.date.today(),help_text='Borrow date',widget=SelectDateWidget())
    borrow_manager = forms.CharField(required=True,help_text="Manager's Initials")#change this to ChoiceField later
    
    class Meta:
        model = Transaction
        fields = ('book','borrower','borrow_date','borrow_manager',)
        #exclude =('idtransaction','renew_date','renew_manager','return_date','return_manager',)

class RenewForm(forms.ModelForm):
    idtransaction = forms.ModelChoiceField(queryset = Transaction.objects.filter(renew_date__isnull = True, return_date__isnull = True),help_text='Transaction')
    renew_date = forms.DateField(required=True,initial=datetime.date.today(),widget=SelectDateWidget(),help_text='Renew Date')
    renew_manager = forms.CharField(required=True,help_text="Manager's Initials")#change this to ChoiceField later
    
    class Meta:
        model = Transaction
        fields = ('idtransaction','renew_date','renew_manager',)
        #exclude = ('book','borrower','borrow_date','borrow_manager','return_date','return_manager',)
        
class ReturnForm(forms.ModelForm):
    idTransaction = forms.ModelChoiceField(queryset = Transaction.objects.filter(return_date__isnull = True),help_text='Transaction')
    return_date = forms.DateField(required=True,initial=datetime.date.today(),widget=SelectDateWidget(),help_text='Return Date')
    return_manager = forms.CharField(required=True,help_text="Manager's Initials")#change this to ChoiceField later
    
    class Meta:
        model = Transaction
        fields = ('idtransaction','return_date','return_manager',)
        #exclude = ('book','borrower','borrow_date','borrow_manager','renew_date','renew_manager',)

class AddBorrowerForm(forms.ModelForm):
    name = forms.CharField(required=True,help_text='Name of Borrower')
    phone = forms.CharField(required=True,help_text='Phone/Mobile Number')
    email = forms.EmailField(required=False,help_text='Email') #some do not have/use email
    cellgroup = forms.CharField(required=True,help_text='Cell group')
    
    def clean(self):
        """
        check for duplications.
        """
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        phone = cleaned_data.get('phone')
        if name and phone:
            #Only when both fields are valid so far.
            try:
                Borrower.objects.get(name=name,phone=phone)
            except Borrower.DoesNotExist:
                pass
            else:
                raise ValidationError(_('This borrower already exists in the database.'),code='invalid')
            return cleaned_data
    
    class Meta:
        model = Borrower
        fields = ('name','phone','email','cellgroup',)
