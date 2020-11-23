"""Chat utils"""

# Utils
from io import StringIO
import csv
import requests

# Models
from chat.models import Message


def get_last_fifteen_messages():
    """Return the las fifteen messages."""
    return Message.objects.all().order_by('created')[:50]


def get_stock(stock):
    """Handle the request to api to get stock value"""
    response = requests.get(
        f'https://stooq.com/q/l/?s={stock}&f=sd2t2ohlcv&h&e=csv%E2%80%8B'
    )
    file = StringIO(response.text)
    stock = csv.DictReader(file)
    row = next(stock)
    if row['Close'] == 'N/D':
        return '{} quote does not have data'.format(row['Symbol'])
    return '{} quote is {} per share'.format(row['Symbol'], row['Close'])
