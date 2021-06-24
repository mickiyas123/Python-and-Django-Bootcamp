import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")


import django
django.setup()


from APPTwo.models import User
from faker import Faker
fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        name=fakegen.name().split()
        fname=fakegen.first_name()
        lname=fakegen.last_name()
        email=fakegen.email()

        user=User.objects.get_or_create(first_name=fname,last_name=lname,email=email)[0]
if __name__=="__main__":
    print("Populating Code")
    populate(20)
    print("Populating Done")
