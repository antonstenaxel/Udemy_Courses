import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_exercise.settings')

import django
django.setup()

#Fake POP script

import random
from App_One.models import user
from faker import Faker
fakegen = Faker('sv_SE');


def populate(N=5):
    for entry in range(N):
        #create fake data for entry
        fake_fn = fakegen.first_name()
        fake_ln = fakegen.last_name()
        fake_email = fake_fn+"_"+fake_ln+"@gmail.com"
        
        # Create new webpage entry
        u = user.objects.get_or_create(first_name = fake_fn, last_name = fake_ln, email = fake_email)[0]
        u.save()

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print('populating complete!')
