from typing import Any
from django.core.management.base import BaseCommand
from dataentry.models import Student

# insert data to the database using insert command 


class Command(BaseCommand):
    help  = "Command to insert data to Database"

    def handle(self, *args: Any, **options: Any) :
        dataset = [
            { "roll_no": "31", "firstName" :"obum", "Age": 40},
            { "roll_no": "34", "firstName" :"ike", "Age": 42},
            { "roll_no": "55", "firstName" :"chi", "Age": 44},
        ]
        for data in dataset:
            roll_no = data["roll_no"]
            existing_record = Student.objects.filter(roll_no=roll_no)
            if not existing_record:
                Student.objects.create(roll_no = data["roll_no"], firstName = data["firstName"], Age = data["Age"])
        self.stdout.write(self.style.SUCCESS("Data Inserted Successfully"))

        