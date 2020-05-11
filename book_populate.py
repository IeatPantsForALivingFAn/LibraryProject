import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','library.settings')

import django
django.setup()

#population code
import random
from books.models import *
from faker import Faker
import random
fake = Faker()

def book_gen(N=5):
    for _ in range(N):
        book = Book.objects.get_or_create(name=fake.company(),author=fake.name(),copies=random.randrange(0,50))[0]
        book.save()

if __name__=='__main__':
    print('Populating script')
    book_gen(100)
    print('Populated Book')
