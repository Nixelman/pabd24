"""Download selected files from S3 storage"""


import argparse

from dotenv import dotenv_values
import boto3

BUCKET_NAME = 'pabd24'
YOUR_ID = '20'
CSV_PATH = ['data/raw/1__0_36__12_5_2024.csv',
            'data/raw/2__0_45__12_5_2024.csv',
            'data/raw/3__0_53__12_5_2024.csv']

config = dotenv_values(".env")


client = boto3.client(
    's3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id=config['KEY'],
    aws_secret_access_key=config['SECRET']
)

def main(args):
    for csv_path in args.input:
        object_name = f'{YOUR_ID}/' + csv_path.replace('\\', '/')
        client.download_file(BUCKET_NAME, object_name, csv_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='+',
                        help='Input local data files to upload to S3 storage',
                        default=CSV_PATH)
    args = parser.parse_args()
    main(args)