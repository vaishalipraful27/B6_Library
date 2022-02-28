from django.db import models

# Create your models here.
print("in models.py")
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()


    class Meta:
        db_table = "book"

    def __str__(self):
        return f"{self.name}"
        

