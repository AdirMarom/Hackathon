import csv

import pandas


def fix_csv():
    colnames = ['query', 'tweet', ]
    colnames_1 = ['query', 'tweet', 'label']
    data = pandas.read_csv('from_moodle.csv', names=colnames)
    data_to_change = pandas.read_csv('with_label.csv', names=colnames_1)
    label = data_to_change['label'].tolist()
    data["label"] = label
    csv_list = []
    for index, row in data.iterrows():
        csv_list.append(row)
    with open('outcome.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_list)

x=fix_csv()