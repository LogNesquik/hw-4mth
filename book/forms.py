from django import forms
from book.models import BookQuote

class BookQuoteForms(forms.ModelForm):
    class Meta:
        model = BookQuote
        fields = "__all__"