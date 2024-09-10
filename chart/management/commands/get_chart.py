from django.core.management import BaseCommand

from chart.cron import collect_chart


class Command(BaseCommand):
    help = "Сохранить текущий чарт Яндекс Музыки"

    def handle(self, *args, **options) -> None:
        collect_chart()
