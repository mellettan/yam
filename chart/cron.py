import os

from dotenv import load_dotenv
from loguru import logger
from yandex_music import Chart as YMChart
from yandex_music import Client, Playlist, Track

from chart.models import Chart

load_dotenv()


def collect_chart() -> int:
    """
    Сохраняет текущий чарт Яндекс Музыки (Россия) в базу и возвращает число треков.
    """
    client = Client(os.getenv("YANDEX_TOKEN")).init()
    logger.info("Получаю чарт России")
    try:
        playlist: Playlist = client.chart("russia").chart
    except Exception as exc:
        logger.error(f"Не удалось получить чарт: {exc}")
        return 0

    entries = []
    for track_short in playlist.tracks:
        track: Track = track_short.track
        position: YMChart = track_short.chart
        entries.append(
            Chart(
                position=position.position,
                name=track.title,
                artists=[artist.name for artist in track.artists or []],
                track_id=track.id,
            )
        )
    Chart.objects.bulk_create(entries)
    logger.info(f"Сохранено треков: {len(entries)}")
    return len(entries)
