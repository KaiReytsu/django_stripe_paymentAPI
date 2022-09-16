from django.db import models


class Item(models.Model):
    '''Fields of the item model'''
    name = models.CharField(verbose_name='Item name', unique=True , max_length=20)
    description = models.CharField(verbose_name='Description', max_length=200)
    price = models.PositiveIntegerField(verbose_name='Price')

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


