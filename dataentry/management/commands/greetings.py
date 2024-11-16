from typing import Any
from django.core.management.base import BaseCommand, CommandParser



# Command to greet user based on passed name 
class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help="The name to greet")

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        name = kwargs['name']

        self.stdout.write(self.style.SUCCESS(f"Hi {name}, Good Morning "))