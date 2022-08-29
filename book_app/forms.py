from django import forms
from book_app.models import book, authors, Shelves


class bookname(forms.ModelForm):
    class Meta():
        model=book
        fields ='__all__'


class authrname(forms.ModelForm):
    class Meta():
        model=authors
        fields ='__all__'


class Shelvesname(forms.ModelForm):
    class Meta():
        model=Shelves
        fields ='__all__'