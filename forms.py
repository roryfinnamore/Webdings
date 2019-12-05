from django import forms
from django.forms import DateTimeField
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.Form):
    date = forms.DateField(widget=DateInput, label="Date")
    title = forms.CharField(max_length=200, label="Event")
    notes = forms.CharField(label="Notes")

category_choices = (
    ('flowers','Flowers'),
    ('cake','Cake'),
    ('venue','Venue'),
    ('catering','Catering'),
    ('decor','Decor'),
    ('beauty','Beauty'),
    ('music','Music'),
    ('photos','Photography'),
    ('transport','Transport'),
    ('favours','Favours'),
)

class SupplierForm(forms.Form):
    category = forms.CharField(label="Category", widget=forms.Select(choices=category_choices))
    supplier = forms.CharField(max_length=200)
    cost = forms.CharField()
    contact = forms.CharField()

class NoteForm(forms.Form):
    note = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":20}))
    person_responsible = forms.CharField()

class BoardForm(forms.Form):
    board = forms.URLField()

class GuestForm(forms.Form):
    guest_name = forms.CharField()
    email = forms.CharField(max_length=200)
