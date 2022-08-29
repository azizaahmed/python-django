from django.shortcuts import render
from book_app.forms import bookname, authrname , Shelvesname
# Create your views here.
def index(request):
    return render(request,'book_app/index.html')

def book(request):
    book =bookname()

    if request.method=='POST':
       form = bookname(request.POST)
       if form.is_valid():
           form.save(commit=True)
           return index(request)
       else:
           print('ERROR FROM INVAID') 
    
    return render(request,'book_app/books.html',{'book': book})

def authors(request):
    authors= authrname()
    if request.method=='POST':
       form = authrname(request.POST)
       if form.is_valid():
           form.save(commit=True)
           return index(request)
       else:
           print('ERROR FROM INVAID')
    return render(request,'book_app/authors.html',{'authors':authors})

def Shelves(request):
    Shelves = Shelvesname()
    if request.method=='POST':
       form = Shelvesname(request.POST)
       if form.is_valid():
           form.save(commit=True)
           return index(request)
       else:
           print('ERROR FROM INVAID')
    return render(request,'book_app/Shelves.html',{'shelves':Shelves})
