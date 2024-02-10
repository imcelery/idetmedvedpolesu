from django.db import models

class Category(models.Model):
    name = models.CharField("Название", max_length=20)


class Good(models.Model):
    name = models.CharField("Название", max_length=20)
    description = models.TextField("Описание")
    price = models.IntegerField("Цена", default=0)

