from socket import fromshare
from tkinter import N
from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    phone = forms.CharField(max_length=200)