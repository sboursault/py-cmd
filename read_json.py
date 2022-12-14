from datetime import datetime
import json


def run():
    f = open('data_samse_3.json')

    data = json.load(f)

    for idx, item in enumerate(data):
        if 'lastChangeDate' in item.keys() and 'creationDate' in item.keys():
            last_change_date = datetime.fromisoformat(item['lastChangeDate'])
            creation_date = datetime.fromisoformat(item['creationDate'])
            if last_change_date < creation_date:
                print(item)

    f.close()


if __name__ == '__main__':
    run()
