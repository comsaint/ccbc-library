from django.shortcuts import render
from ccbclib.forms import BorrowForm, ReturnForm, RenewForm
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from ccbclib.models import Book, Borrower, Transaction
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django_tables2 import RequestConfig
from ccbclib.tables import BookTable, BorrowerTable, TransactionTable
#from statistics import mode
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User

def about(request):
    context_dict = {}
    return render(request, 'ccbclib/about.html', context_dict)

@login_required
def home(request):
    context_dict = {}
    return render(request, 'ccbclib/home.html', context_dict)

@login_required
def success(request):
    context_dict={}
    return render(request, 'ccbclib/operation_successful.html',context_dict)

@login_required
def bookborrow(request):
    staffname = get_staffname(request)
        
    # A HTTP POST?
    if request.method == 'POST':
        form = BorrowForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            tmp_tran = form.save(commit=False)
            tmp_tran.borrow_manager = staffname
            tmp_tran.save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return HttpResponseRedirect(reverse('ccbclib:success'))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = BorrowForm()


    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'ccbclib/borrow.html', {'form': form,'staffname':staffname})

@login_required
def bookreturn(request):
    staffname = get_staffname(request)
        
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            transaction = Transaction.objects.get(pk=form.cleaned_data['idtransaction'].idtransaction)
            form = ReturnForm(request.POST, instance=transaction)
            tmp_tran = form.save(commit=False)
            tmp_tran.return_manager = staffname
            tmp_tran.save()
            # Now call the home() view.
            # The user will be shown the homepage.
            return HttpResponseRedirect(reverse('ccbclib:success'))
        else:
            print(form.errors)
    else:
        form = ReturnForm()
        staffname = request.user.get_full_name()
        if staffname=="":
            staffname = request.user.get_username()
    return render(request, 'ccbclib/return.html', {'form': form,'staffname':staffname})

@login_required
def bookrenew(request):
    staffname = get_staffname(request)
        
    if request.method == 'POST':
        form = RenewForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            transaction = Transaction.objects.get(pk=form.cleaned_data['idtransaction'].idtransaction)
            form = RenewForm(request.POST, instance=transaction)
            tmp_tran = form.save(commit=False)
            tmp_tran.renew_manager = staffname
            tmp_tran.save()
            return HttpResponseRedirect(reverse('ccbclib:success'))
        else:
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = RenewForm()
        

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'ccbclib/renew.html', {'form': form,'staffname':staffname})

@login_required
def infotable(request,dataToDisplay):
    if dataToDisplay == 'transactions':
        table = TransactionTable(Transaction.objects.all())
        RequestConfig(request).configure(table)
        context_dict = {
                   "info_title" : "Transactions",
                   "table" : table
                   }
    elif dataToDisplay == 'books':
        table = BookTable(Book.objects.all())
        RequestConfig(request).configure(table)
        context_dict = {
                   "info_title": "Books",
                   "table" : table
                   }
    elif dataToDisplay == 'borrowers':
        table = BorrowerTable(Borrower.objects.all())
        RequestConfig(request).configure(table)
        context_dict = {
                   "info_title": "Borrowers",
                   "table" : table
                   }
    else:
        return HttpResponse("Cannot find resources specified.")
    
    return render(request,"ccbclib/info_table.html",context_dict)


##django's built-in generic view.
# CRUD for Book model
"""
# We may not want to add/modify/delete a book in normal applications - or set higher permission for this?

class BookCreate(CreateView):
    model = Book
    fields = ['name','code']
    success_url = reverse_lazy('ccbclib:success')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name','code']

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')
"""
# CRUD for Borrower model

class BorrowerListView(ListView):
    model = Borrower


class BorrowerCreate(CreateView):
    model = Borrower
    fields = ['name','phone','email','cellgroup']
    success_url = reverse_lazy('ccbclib:success')


class BorrowerUpdate(UpdateView):
    model = Borrower
    fields = ['name','phone','email','cellgroup']
    success_url = reverse_lazy('ccbclib:success')

"""
class BorrowerDelete(DeleteView):
    model = Borrower
    fields = ['name','phone','email','cellgroup']
    success_url = reverse_lazy('ccbclib:success')
"""
# No easy generic edit views for Transaction model

#Some custom functions
def get_staffname(request):
    staffname = request.user.get_full_name()
    if staffname=="":
        staffname = request.user.get_username()
    return staffname