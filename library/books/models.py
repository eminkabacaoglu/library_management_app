from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True) #zorunlu alan değil
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='books') # related_name tanımlaması author nesnesi uzerinden ilişkili ldugu book nesnelerine erişim için kulanılır
    isbn = models.CharField(max_length=13, unique=True) #unique bir değer
    genre = models.CharField(max_length=255)
    
    publication_date = models.DateField()
    
    def __str__(self):
        return f"{self.title} - {self.author.name}"