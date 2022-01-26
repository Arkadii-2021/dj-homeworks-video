from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=250)
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=64, unique=True, db_index=True)

    def __str__(self):
        return f'{self.name}, {self.image}, {self.price}, {self.release_date}, {self.lte_exists}, {self.slug}'


