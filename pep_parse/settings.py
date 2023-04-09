BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

DATE_FORMAT = '%Y-%m-%dT%H-%M-%S'
RESULTS = 'results'
STATUS = 'Status'
AMOUNT = 'Amount'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
