from faker import Faker
from openpyxl import Workbook


def get_data():
    fk = Faker()
    return [[fk.name(), fk.address(), fk.phone_number()] for _ in range(100)]

def get_excel():
    wb = Workbook()
    ws = wb.active
    for row in get_data():
        ws.append(row)
    wb.save('test.xlsx')

def main():
    get_data()
    get_excel()



if __name__ == "__main__":
    main()

