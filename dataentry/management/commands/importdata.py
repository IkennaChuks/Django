from typing import Any
from django.apps import apps
from django.core.management.base import BaseCommand, CommandParser, CommandError
from dataentry.models import Student
import csv 

class Command(BaseCommand):
    # python manage.py importdata csv_file
    help = "Import large dataset to the Database using a csv"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("file_path", type=str,help="Path to CSV file")
        parser.add_argument("model_name", type=str,help="Model to load")

    def handle(self, *args: Any, **options: Any) :
        file_path = options["file_path"]
        model_name = options["model_name"].capitalize()

        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label,model_name)
                break # Stop searching once model is found
            except LookupError as l:
                continue # continue searching in next app 

        if not model :
            raise CommandError(f"Model {model_name} not found in any app")
        
        else :

            with open(file_path, "r" ) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    model.objects.create(**row)
            self.stdout.write(self.style.SUCCESS("Data Imported Successfully!"))

