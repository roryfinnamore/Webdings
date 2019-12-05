from django.db import models
from datetime import datetime

class Event(models.Model):
    event_date = models.DateField(default=datetime.now, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Timelines"

class Guest(models.Model):
    guest_name = models.TextField()
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.guest_name
        
    class Meta:
        verbose_name_plural = "Guests"

class Note(models.Model):
    note = models.TextField()
    person_responsible = models.TextField()
    
    
    def __str__(self):
        return self.note
        
    class Meta:
        verbose_name_plural = "Notes"

category_choices = (
    ('Flowers','Flowers'),
    ('Cake','Cake'),
    ('Venue','Venue'),
    ('Catering','Catering'),
    ('Decor','Decor'),
    ('Beauty','Beauty'),
    ('Music','Music'),
    ('Photos','Photography'),
    ('Transport','Transport'),
    ('Favours','Favours'),
)

class Supplier(models.Model):
    category = models.TextField(choices=category_choices)
    supplier = models.CharField(max_length=200)
    cost = models.IntegerField()
    contact = models.TextField()
    
    def __str__(self):
        return self.supplier
        
    class Meta:
        verbose_name_plural = "Suppliers"

class Board(models.Model):
    board = models.URLField()
       
    
    def __str__(self):
        return self.board
        
    class Meta:
        verbose_name_plural = "Boards"

class Aim(models.Model):
    aim = models.CharField(max_length=300)
       
    def __str__(self):
        return self.aim
        
    class Meta:
        verbose_name_plural = "Aims"

