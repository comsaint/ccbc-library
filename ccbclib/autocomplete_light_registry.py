import autocomplete_light
from ccbclib.models import Book
#from autocomplete_light.tests.autocomplete import search_fields

class BookAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['code_number']
    model = Book
    #choices = Book.objects.all() #then use choices_for_request() for filtering
    attrs={
        'placeholder': 'Code number of the book',
        'data-autocomplete-minimum-characters': 5,
        },
    widget_attrs={
        'data-widget-maximum-values': 10,
        'class': 'modern-style',
        },
    #dynamic filtering, return only books available (quantity>0)
    def choices_for_request(self):
        self.choices = self.choices.filter(quantity__gt=0)
        return super(BookAutocomplete,self).choices_for_request()
autocomplete_light.register(BookAutocomplete)