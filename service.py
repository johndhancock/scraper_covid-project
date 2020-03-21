from utils import upload_data_s3

import scraper
import json

def handler(event, context):
    print('service started')

    data = json.dumps(scraper.perform_scrape())
    bucket_filepath = 'data-store/2020/tx-coronavirus.json'

    upload_data_s3(data, bucket_filepath, 'json')
# this function is just for our testing purposes,
# just calling the main handler function
if __name__ == '__main__':
    handler(1, 2)
