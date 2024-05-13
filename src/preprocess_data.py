"""Transform raw data to train / val datasets """
import argparse
import logging
import pandas as pd
import numpy as np
from sklearn.utils import shuffle

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='log/preprocess_data.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')


IN_FILES = ['data/raw/1__0_36__12_5_2024.csv',
            'data/raw/2__0_45__12_5_2024.csv',
            'data/raw/3__0_53__12_5_2024.csv']

OUT_TRAIN = 'data/proc/train.csv'
OUT_VAL = 'data/proc/val.csv'

TRAIN_SIZE = 0.9


def main(args):
    main_dataframe = pd.read_csv(args.input[0], delimiter=',')
    for i in range(1, len(args.input)):
        data = pd.read_csv(args.input[i], delimiter=',')
        df = pd.DataFrame(data)
        main_dataframe = pd.concat([main_dataframe, df], axis=0)

    # main_dataframe['url_id'] = main_dataframe['url'].map(lambda x: x.split('/')[-2])
    main_dataframe['url_id'] = main_dataframe['url'].apply(lambda x: x.split('/')[-2] if isinstance(x, str) else np.nan)
    new_dataframe = main_dataframe[['url_id', 'total_meters', 'price']].set_index('url_id')

    new_df = new_dataframe[new_dataframe['price'] < 30_000_000]
    new_df = shuffle(new_df)


    border = int(args.split * len(new_df))
    train_df, val_df = new_df[0:border], new_df[border:-1]
    train_df.to_csv(OUT_TRAIN)
    val_df.to_csv(OUT_VAL)
    logger.info(f'Write {args.input} to train.csv and val.csv. Train set size: {args.split}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--split', type=float,
                        help='Split test size',
                        default=TRAIN_SIZE)
    parser.add_argument('-i', '--input', nargs='+',
                        help='List of input files',
                        default=IN_FILES)
    args = parser.parse_args()
    main(args)