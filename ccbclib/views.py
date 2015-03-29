from django.shortcuts import render
from ccbclib.forms import BorrowForm, ReturnForm, RenewForm, AddBorrowerForm
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ccbclib.models import Book, Borrower, Transaction

from django_tables2 import RequestConfig
from ccbclib.tables import BookTable, BorrowerTable, TransactionTable

def index(request):
    return HttpResponse("Welcome to CCBC Library!")

def about(request):
    context_dict = {}
    return render(request, 'ccbclib/about.html', context_dict)

def home(request):
    context_dict = {}
    return render(request, 'ccbclib/home.html', context_dict)

def success(request):
    context_dict={}
    return render(request, 'ccbclib/operation_successful.html',context_dict)

def bookborrow(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = BorrowForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

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
    return render(request, 'ccbclib/borrow.html', {'form': form})

def bookreturn(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            transaction = Transaction.objects.get(pk=form.cleaned_data['idTransaction'].idTransaction)
            form = ReturnForm(request.POST, instance=transaction)
            form.save()

            # Now call the home() view.
            # The user will be shown the homepage.
            return HttpResponseRedirect(reverse('ccbclib:success'))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = ReturnForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'ccbclib/return.html', {'form': form})

def bookrenew(request):
    if request.method == 'POST':
        form = RenewForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            transaction = Transaction.objects.get(pk=form.cleaned_data['idtransaction'].idtransaction)
            form = RenewForm(request.POST, instance=transaction)
            form.save()

            # Now call the home() view.
            # The user will be shown the homepage.
            return HttpResponseRedirect(reverse('ccbclib:success'))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = RenewForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'ccbclib/renew.html', {'form': form})

def addborrower(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = AddBorrowerForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('ccbclib:success'))
        else:
            # Display error on the template.
            return render(request, 'ccbclib/addborrower.html', {'form': form})
    else:
        # If the request was not a POST, display the form to enter details.
        form = AddBorrowerForm()
    return render(request, 'ccbclib/addborrower.html', {'form': form})


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