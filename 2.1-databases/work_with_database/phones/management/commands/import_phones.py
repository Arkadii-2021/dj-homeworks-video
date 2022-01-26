import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
import re


def convert_name_to_slug(slug_name):
    result = re.sub(r' ', '-', slug_name)
    return result


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_list = Phone.objects.create(
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=str(phone['name']).replace(' ', '-')
            )
            phone_list.save()
            print(f'{phone} в базу добавлен')

