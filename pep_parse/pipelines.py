import csv

from collections import defaultdict
from datetime import datetime
from pathlib import Path

from pep_parse.settings import AMOUNT, DATE_FORMAT, RESULTS, STATUS

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.all_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.all_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.all_statuses.values())
        datetime_now = datetime.now().strftime(DATE_FORMAT)
        filename = f'status_summary_{datetime_now}.csv'
        result_path = BASE_DIR / RESULTS / filename
        with open(f'{result_path}', mode='w', encoding='utf-8') as csvfile:
            fieldnames = [STATUS, AMOUNT]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for status, amount in self.all_statuses.items():
                writer.writerow({STATUS: status, AMOUNT: amount})
            writer.writerow({STATUS: 'Total', AMOUNT: total})
