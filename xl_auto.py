import pandas
import tools
import numpy

fileName = r"./EU Sales Report.xls"

df = pandas.read_csv(fileName, encoding=tools.detect_encoding(fileName), sep="\t")
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
