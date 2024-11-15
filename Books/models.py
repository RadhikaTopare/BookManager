from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    
    STATUS_CHOICES = [
        ('R','Read'),
        ('U', 'Unread'),
    ]
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Biography', 'Biography'),
        ('Drama', 'Drama'),
        ('Romantic','Romantic'),
        ('Comedy', 'Comedy'),
        ('War', 'War'),
        ('Gangster', 'Gangster'),
        ('Horror', 'Horror'),
        ('Finance','Finance'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    rating = models.IntegerField(null= True,blank=True)
    publish_date = models.DateField(null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='U')
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

def __str__ (self):
    return f"{self.title} by {self.author}"