from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Команда для загрузки всех фикстур одной командой."""

    help = 'Загрузка всех фикстур одной командой'

    def handle(self, *args, **options):
        FIXTURES = [
            'fixtures/users.csv',
            'fixtures/categories.csv',
            'fixtures/subcategories.csv',
            'fixtures/products.csv',
            'fixtures/cart.csv'
        ]
        for fixture in FIXTURES:
            call_command('load_csv', fixture)
        self.stdout.write(
            self.style.SUCCESS("Загрузка всех фикстур завершена!"))
