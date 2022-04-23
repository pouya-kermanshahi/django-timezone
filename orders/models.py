from django.db import models

# Create your models here.


class Order(models.Model):

    name = models.CharField(max_length=400)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"
