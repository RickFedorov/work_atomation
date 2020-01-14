import pandas
import chardet
import numpy

fileName = r"./EU Sales Report.xls"

# detect encoding
detector = chardet.UniversalDetector()
for line in open(fileName, 'rb'):
    detector.feed(line)
    if detector.done: break
detector.close()

df = pandas.read_csv(fileName, encoding=detector.result['encoding'], sep="\t")
print(next(df.iterrows())[1])

new_row = {
    'Country': "",
    'Tax No.': "",
    'Customer Code': "",
    'Customer Name': ""
}

for index, row in df.iterrows():

    if not pandas.isna(row['Country']):
        new_row['Country'] = row['Country']
    print(new_row['Country'])


def main():
    pass


if __name__ == '__main__':
    main()
