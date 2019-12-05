from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from .forms import *

def index(request):
    return render(request,'webdings/dashboard.html')

def timeline(request):
    events = Event.objects.order_by('event_date')[:10]   

    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            date = form.cleaned_data['date']
            event = form.cleaned_data['title']
            notes = form.cleaned_data['notes']
            e = Event(event_date=date, title=event,body=notes)
            e.save()
            return HttpResponseRedirect('/webdings/timeline')
    else:
        form = EventForm()

    context = {
        'title':'TIMELINE',
        'events':events,
        'form':form
    }
    return render(request,'webdings/timeline.html',context)

def shortlists(request):
    suppliers = Supplier.objects.order_by('category','cost')[:10]
    
    if request.method == "POST":
        form = SupplierForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']
            supplier = form.cleaned_data['supplier']
            cost = form.cleaned_data['cost']
            contact = form.cleaned_data['contact']
            s = Supplier(category=category, supplier=supplier, cost=cost, contact=contact)
            s.save()
            return HttpResponseRedirect('/webdings/shortlists')
    else:
        form = SupplierForm() 

    context = {
        'title':'SUPPLIER SHORTLIST',
        'suppliers':suppliers,
        'form':form
    }
    return render(request,'webdings/shortlists.html',context)

def concepts(request):
    boards = Board.objects.all()[:10]
    
    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            board = form.cleaned_data['board']
            b = Board(board=board)
            b.save()
            return HttpResponseRedirect('/webdings/concepts')
    else:
        form = BoardForm() 

    context = {
        'boards':boards,
        'form':form
    }
    return render(request,'webdings/concepts.html',context)

def notes(request):
    notes = Note.objects.all()[:10]
    
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.cleaned_data['note']
            person_responsible = form.cleaned_data['person_responsible']
            n = Note(note=note,person_responsible=person_responsible)
            n.save()
            return HttpResponseRedirect('/webdings/notes')
    else:
        form = NoteForm() 

    context = {
        'title':'Notes',
        'notes':notes,
        'form':form
    }
    return render(request,'webdings/notes.html',context)

def guests(request):
    guests = Guest.objects.all()[:10]
    
    if request.method == "POST":
        form = GuestForm(request.POST)

        if form.is_valid():
            guest_name = form.cleaned_data['guest_name']
            email = form.cleaned_data['email']
            g = Guest(guest_name=guest_name,email=email)
            g.save()
            return HttpResponseRedirect('/webdings/guests')
    else:
        form = GuestForm() 

    context = {
        'title':'Guests',
        'guests':guests,
        'form':form
    }
    return render(request,'webdings/guests.html',context)
    

