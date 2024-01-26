from django.db import models

# Create your models here.


class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    Book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return self.Book_name + "   " + self.author
