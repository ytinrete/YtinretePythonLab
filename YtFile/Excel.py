
import csv
from openpyxl import load_workbook
import xlrd

#pip3 install openpyxl
#pip3 install xlrd

def read_csv():
    try:
        res = []
        table_name = 'unknown'
        with open("../TestFile/Excel/query_result.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = {}
                obj['data'] = {}
                for (k, v) in row.items():
                    pos = k.index('.')
                    table_name = k[0:pos]
                    col = k[pos + 1:]
                    obj['table'] = table_name
                    if col == 'eventtime':
                        obj['eventtime'] = v
                    elif col == 'sessionid':
                        obj['sessionid'] = v
                    elif col == 'eventname':
                        obj['eventname'] = v
                    elif col == 'test_data_deviceid':
                        obj['test_data_deviceid'] = v
                    elif col == 'appkey':
                        obj['appkey'] = v
                    elif col == 'dt':
                        obj['dt'] = v
                    else:
                        obj['data'][col] = v

                res.append(obj)

        return res, table_name
    except BaseException as e:
        print(e)


def read_xlsx():
    wb = load_workbook(filename='../TestFile/Excel/Test.xlsx')
    sheet_ranges = wb['工作表1']
    print(sheet_ranges['A2'].value)
    pass

def read_xls():
    wb = xlrd.open_workbook('../TestFile/Excel/Test.xls')
    sh = wb.sheet_by_index(0)
    # print(sh.cell(2, 2).value)
    print(sh.row_values(1)[0])
    pass


if __name__ == '__main__':
    cvs_list, name = read_csv()

    for item in cvs_list:
        print(item)

    read_xlsx()

    read_xls()

    pass