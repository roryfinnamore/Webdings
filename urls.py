from django.urls import path
from . import views

urlpatterns = [

    path("dashboard",views.index,name="index"),
    path("timeline",views.timeline,name="timeline"),
    path("shortlists",views.shortlists,name="shortlists"),
    path("concepts",views.concepts,name="concepts"),
    path("notes",views.notes,name="notes"),
    path("guests",views.guests,name="guests"),

]