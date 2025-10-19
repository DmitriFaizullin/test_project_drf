import csv
import os
import re

from django.core.management.base import BaseCommand

from ._private import CommandMixin


class Command(BaseCommand, CommandMixin):
    """Менеджер для загрузки csv-файлов."""

    help = '''Для корректной загрузки информации в базу
        названия файлов и порядок загрузки следующий:
        users.csv, category.csv, subcategory.csv, products.csv, cart.csv'''

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Путь к CSV файлу')

    def handle(self, *args, **options):
        csv_file = options.get('csv_file', '')

        if not os.path.isfile(csv_file):
            self.stdout.write(self.style.ERROR(f'Файл {csv_file} не найден!'))
            return

        with open(csv_file, newline='', encoding='utf-8') as file:
            table_name = re.split(r'[/.]', csv_file)[-2]
            if table_name not in self.TABLE_HANDLER:
                self.stdout.write(self.style.ERROR(
                    f'Обработчик для таблицы {table_name} не найден!'
                ))
                return
            self.csvreader = csv.DictReader(file)
            self.TABLE_HANDLER[table_name](self)
            self.stdout.write(self.style.SUCCESS(
                f'Загрузка данных из {csv_file} завершена'
            ))
