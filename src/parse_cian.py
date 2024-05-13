""""""
import cianparser
import pandas as pd
import datetime
# from dotenv import dotenv_values
# import boto3


# config = dotenv_values(".env")
# client = boto3.client(
#     "s3",
#     endpoint_url = "https://storage.yandexcloud.net",
#     aws_access_key_id = config["KEY"],
#     aws_secret_access_key = config["SECRET"]
# )

moscow_parser = cianparser.CianParser(location="Москва")


def main():
    """"""
    n_rooms = 3
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=(n_rooms,),
        # with_saving_csv=True,
        additional_settings={
            "start_page": 1,
            "end_page": 50,
            "object_type": "secondary"
        })
    df = pd.DataFrame(data)
    csv_path = f"data/raw/{n_rooms}__{datetime.datetime.now().hour}_{datetime.datetime.now().minute}__{datetime.datetime.now().day}_{datetime.datetime.now().month}_{datetime.datetime.now().year}.csv"
    df.to_csv(csv_path)
    # bucket_name = "pabd24"
    # object_name = "20/" + csv_path
    # client.upload_file(csv_path, bucket_name, object_name)


if __name__ == '__main__':
    main()
