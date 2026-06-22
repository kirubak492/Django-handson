from blog.models import Category
from typing import Any
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help= "This commands insert category data" #manual command creation

    def handle(self,*args:Any,**options:Any):


        Category.objects.all().delete()
        
        categories=['Sports', 'Technology', 'Science', 'Arts','Food']
        
        for category in categories:
             
             Category.objects.create(name=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))

