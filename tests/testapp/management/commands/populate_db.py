# -*- coding: utf-8 -*-

import random
import string
from django.core.management.base import BaseCommand
from tests.testapp import models
from tests.testapp.models import *


def random_string(n):
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(n)
    )


def random_name(n):
    words = ''.join(random.choice(string.ascii_lowercase + ' ') for _ in range(n)).strip().split(' ')
    return '-'.join([x.capitalize() for x in words])


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Genre.objects.bulk_create([Genre(pk=pk, title=random_string(50)) for pk in range(100)])
        # Artist.objects.bulk_create([Artist(pk=pk, title=random_string(50)) for pk in range(100)])
        countries = Country.objects.bulk_create([Country(pk=pk, name=random_name(random.randint(10, 20))) for pk in range(10)] )
        City.objects.bulk_create([City(pk=pk, name=random_name(random.randint(5, 15)), country=random.choice(countries)) for pk in range(100)] )
