from django.db import models


#Authors (Id, Name, Email)
class authors(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300 , unique=True)

    def __str__(self):
        return self.name


#Shelves (Id, Name)
class Shelves(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name

# Books (Id, Title, Abstract, ISBN, AuthorID, ShelfID)
class book(models.Model):
    title = models.CharField(max_length=300)
    abstract = models.CharField(max_length=400)
    isbn = models.IntegerField()
    authorid = models.ForeignKey(authors, on_delete=models.CASCADE)
    shelfid = models.ForeignKey(Shelves, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
