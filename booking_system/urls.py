from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_a_table, name='book_a_table'),
    path('choose_date/', views.ChooseDateView.as_view(), name='choose_date'),
    path('select_time/', views.SelectTimeView.as_view(), name='select_time'),
   # path('contact_details/', views.ContactDetailsView.as_view(), name='contact_details'),
]