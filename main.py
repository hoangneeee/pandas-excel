import datetime
import time
import math
from typing import List, Tuple, Dict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = './data/Book1.xlsx'

df = pd.read_excel(io=path, sheet_name='Sheet1')

print('Số row:', len(df))

# df.info()

# Col
name = df['Họ và tên'].values
dateOfBirth = df['Năm sinh'].values
genders = df['Giới tính'].values
cardId = df['SỐ CMND'].values
phone = df['Số Điện thoại'].values
salary = df['Lương'].values
address = df['Địa Chỉ'].values
buyOften = df['Loại mặt hàng thường xuyên mua'].values
shop = df['Sàn thương mại yêu thích'].values
maxPayShopping = df['Mức tiền chi trả cho nhu cầu mua hàng onl'].values
level = df['Mức hài lòng'].values
vote = df['Đánh giá sau khi mua'].values
returnProduct = df['Trả hàng'].values
marry = df['Đã có vợ hoặc chồng'].values
financialProblem = df['Gặp vấn đề về tài chính'].values


def veBieuDoTron(data: List[float], labels: List[str]):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    ax.pie(data, labels=labels, autopct='%1.2f%%')
    plt.show()


def veBieuDoCot(data: List[float], labels: List[str], type = 1):
    # Mặc định type = 1 là cột dọc khác 1 là cột ngang
    x = np.array(labels)
    y = np.array(data)
    if type == 1:
        plt.bar(x,y)
        plt.show()
    else:
        plt.barh(x,y)
        plt.show()


def handleDateOfBirth(dataOfBirth: List[datetime.date]):
    timeNow = time.localtime()
    ages: list[int] = []
    rangeAge1: list[int] = []
    rangeAge2: list[int] = []
    rangeAge3: list[int] = []
    rangeAge4: list[int] = []
    rangeAge5: list[int] = []
    rangeAge6: list[int] = []
    for date in dataOfBirth:
        if type(date) is str: continue

        age = timeNow.tm_year - date.year
        ages.append(age)

        # Lấy ra các khoảng tuổi
        if 0 < age <= 14:
            rangeAge1.append(age)
        if 15 < age <= 20:
            rangeAge2.append(age)
        if 21 < age <= 29:
            rangeAge3.append(age)
        if 30 < age <= 45:
            rangeAge4.append(age)
        if 46 < age <= 59:
            rangeAge5.append(age)
        if age > 60:
            rangeAge6.append(age)

    totalAge = sum(ages)
    doTuoiTrungBinh = totalAge / len(ages)
    percentRange1 = sum(rangeAge1) / totalAge * 100
    percentRange2 = sum(rangeAge2) / totalAge * 100
    percentRange3 = sum(rangeAge3) / totalAge * 100
    percentRange4 = sum(rangeAge4) / totalAge * 100
    percentRange5 = sum(rangeAge5) / totalAge * 100
    percentRange6 = sum(rangeAge6) / totalAge * 100
    print('======')
    print('Độ tuổi TB :', doTuoiTrungBinh)
    print('Độ tuổi  0-14:', percentRange1)
    print('Độ tuổi  15-20:', percentRange2)
    print('Độ tuổi  21-29:', percentRange3)
    print('Độ tuổi  30-45:', percentRange4)
    print('Độ tuổi  46-59:', percentRange5)
    print('Độ tuổi  > 60:', percentRange6)
    print('======')
    veBieuDoTron(
        data=[percentRange1, percentRange2, percentRange3, percentRange4, percentRange5, percentRange6],
        labels=['0-14', '15-20', '21-29', '30-45', '46-59', '> 60']
    )
    veBieuDoCot(
        data=[percentRange1, percentRange2, percentRange3, percentRange4, percentRange5, percentRange6],
        labels=['0-14', '15-20', '21-29', '30-45', '46-59', '> 60'],
    )


def handleGender():
    gendersData: list[str] = []
    rangeGender1: list[str] = []
    rangeGender2: list[str] = []

    for gender in genders:
        if type(gender) is float: continue

        gendersData.append(gender)

        if gender == 'Nữ':
            rangeGender1.append(gender)
        else:
            rangeGender2.append(gender)

    totalGenders = len(gendersData)
    percentRange1 = len(rangeGender1) / totalGenders * 100
    percentRange2 = len(rangeGender2) / totalGenders * 100
    veBieuDoTron(
        data=[percentRange1, percentRange2],
        labels=['Nữ', 'Nam']
    )
    veBieuDoCot(
        data=[percentRange1, percentRange2],
        labels=['Nữ', 'Nam'],
    )


def handleSalary():
    listSalary: List[float] = []

    range1: List[float] = []
    range2: List[float] = []
    range3: List[float] = []
    range4: List[float] = []
    range5: List[float] = []
    range6: List[float] = []

    for ele in salary:

        if math.isnan(ele): continue
        listSalary.append(ele)

        if 900000 <= ele < 5000000:
            range1.append(ele)
        if 5000000 <= ele < 10000000:
            range2.append(ele)
        if 10000000 <= ele < 15000000:
            range3.append(ele)
        if 15000000 <= ele < 20000000:
            range4.append(ele)
        if 20000000 <= ele < 30000000:
            range5.append(ele)
        if ele > 30000000:
            range6.append(ele)

    totalSalary = sum(listSalary)
    percentRange1 = sum(range1) / totalSalary * 100
    percentRange2 = sum(range2) / totalSalary * 100
    percentRange3 = sum(range3) / totalSalary * 100
    percentRange4 = sum(range4) / totalSalary * 100
    percentRange5 = sum(range5) / totalSalary * 100
    percentRange6 = sum(range6) / totalSalary * 100
    print('======')
    print('900k - 5M:', percentRange1)
    print('5M - 10M:', percentRange2)
    print('10M - 15M:', percentRange3)
    print('15M - 20M:', percentRange4)
    print('20M - 30M', percentRange5)
    print('> 30M', percentRange6)
    print('======')
    data=[percentRange1, percentRange2, percentRange3, percentRange4, percentRange5, percentRange6]
    labels=['900k - 5M', '5M - 10M', '10M - 15M', '15M - 20M', '20M - 30M', '> 30M']
    veBieuDoTron(
        data=data,
        labels=labels,
    )
    veBieuDoCot(
        data=data,
        labels=labels
    )


def handleBuyOften():
    datas: List[str] = []

    range1: List[str] = []
    range2: List[str] = []
    range3: List[str] = []
    range4: List[str] = []
    range5: List[str] = []
    range6: List[str] = []
    range7: List[str] = []
    range8: List[str] = []
    range9: List[str] = []
    range10: List[str] = []
    range11: List[str] = []
    range12: List[str] = []
    range13: List[str] = []
    range14: List[str] = []
    range15: List[str] = []
    range16: List[str] = []
    range17: List[str] = []

    dataSet = list(set(buyOften))

    for ele in buyOften:
        if type(ele) is float: continue
        ele1 = ele.strip()

        datas.append(ele1)

        if ele1 == 'Phụ kiện thời trang':
            range1.append(ele1)
        if ele1 == 'Đồ handmade':
            range2.append(ele1)
        if ele1 == 'Thực phẩm sạch':
            range3.append(ele1)
        if ele1 == 'Phụ kiện thời trang':
            range4.append(ele1)
        if ele1 == 'Đồ gia dụng':
            range5.append(ele1)
        if ele1 == 'Phụ kiện điện thoại phụ kiện thú cưng':
            range6.append(ele1)
        if ele1 == 'Đồ ăn vặt':
            range7.append(ele1)
        if ele1 == 'Quà tặng':
            range8.append(ele1)
        if ele1 == 'Quần áo hàng thùng':
            range9.append(ele1)
        if ele1 == 'Quần áo':
            range10.append(ele1)
        if ele1 == 'Đồ theo hot “trend”':
            range11.append(ele1)
        if ele1 == 'Mỹ phẩm':
            range12.append(ele1)
        if ele1 == 'Đồ uống có cồn':
            range13.append(ele1)
        if ele1 == 'Đồ uống giải khát':
            range14.append(ele1)
        if ele1 == 'Mặt hàng cây cảnh trang trí':
            range15.append(ele1)
        if ele1 == 'Phụ kiện thời trang':
            range16.append(ele1)
        if ele1 == 'Giày dép':
            range17.append(ele1)

    total = len(datas)
    percentRange1 = len(range1) / total * 100
    percentRange2 = len(range2) / total * 100
    percentRange3 = len(range3) / total * 100
    percentRange4 = len(range4) / total * 100
    percentRange5 = len(range5) / total * 100
    percentRange6 = len(range6) / total * 100
    percentRange7 = len(range7) / total * 100
    percentRange8 = len(range8) / total * 100
    percentRange9 = len(range9) / total * 100
    percentRange10 = len(range10) / total * 100
    percentRange11 = len(range11) / total * 100
    percentRange12 = len(range12) / total * 100
    percentRange13 = len(range13) / total * 100
    percentRange14 = len(range14) / total * 100
    percentRange15 = len(range15) / total * 100
    percentRange16 = len(range16) / total * 100
    percentRange17 = len(range17) / total * 100
    print('======')
    print('Phụ kiện thời trang:', percentRange1)
    print('Đồ handmade:', percentRange2)
    print('Thực phẩm sạch:', percentRange3)
    print('Phụ kiện thời trang:', percentRange4)
    print('Đồ gia dụng:', percentRange5)
    print('Phụ kiện điện thoại phụ kiện thú cưng:', percentRange6)
    print('Đồ ăn vặt:', percentRange7)
    print('Quà tặng:', percentRange8)
    print('Quần áo hàng thùng:', percentRange9)
    print('Quần áo:', percentRange10)
    print('Đồ theo hot “trend”:', percentRange11)
    print('Mỹ phẩm:', percentRange12)
    print('Đồ uống có cồn:', percentRange13)
    print('Đồ uống giải khát:', percentRange14)
    print('Mặt hàng cây cảnh trang trí:', percentRange15)
    print('Phụ kiện thời trang:', percentRange16)
    print('Giày dép:', percentRange17)
    print('======')
    data=[percentRange1,
          percentRange2,
          percentRange3,
          percentRange4,
          percentRange5,
          percentRange6,
          percentRange7,
          percentRange8,
          percentRange9,
          percentRange10,
          percentRange11,
          percentRange12,
          percentRange13,
          percentRange14,
          percentRange15,
          percentRange16,
          percentRange17,
          ]
    labels=['Phụ kiện thời trang',
            'Đồ handmade',
            'Thực phẩm sạch',
            'Phụ kiện thời trang',
            'Đồ gia dụng',
            'Phụ kiện điện thoại phụ kiện thú cưng',
            'Đồ ăn vặt',
            'Quà tặng',
            'Quần áo hàng thùng',
            'Quần áo',
            'Đồ theo hot “trend”',
            'Mỹ phẩm',
            'Đồ uống có cồn',
            'Đồ uống giải khát',
            'Mặt hàng cây cảnh trang trí',
            'Phụ kiện thời trang',
            'Giày dép',
            ]
    veBieuDoTron(
        data=data,
        labels=labels,
    )
    veBieuDoCot(
        data=data,
        labels=labels
    )


def handleShop():
    datas: List[str] = []

    range1: List[str] = []
    range2: List[str] = []
    range3: List[str] = []
    range4: List[str] = []
    range5: List[str] = []
    range6: List[str] = []
    range7: List[str] = []
    range8: List[str] = []
    range9: List[str] = []

    dataSet = list(set(shop))
    print(dataSet)
    for ele in shop:
        if type(ele) is float: continue

        ele1 = ele.strip()

        datas.append(ele1)

        if ele1 == 'Shoope':
            range1.append(ele1)
        if ele1 == 'Các  Sàn khác':
            range2.append(ele1)
        if ele1 == 'Amazon':
            range3.append(ele1)
        if ele1 == 'Sendo':
            range4.append(ele1)
        if ele1 == 'Lazada':
            range5.append(ele1)
        if ele1 == '1688':
            range6.append(ele1)
        if ele1 == 'Facebook':
            range7.append(ele1)
        if ele1 == 'Alibaba':
            range8.append(ele1)
        if ele1 == 'TiktokShop':
            range9.append(ele1)

    total = len(datas)
    percentRange1 = len(range1) / total * 100
    percentRange2 = len(range2) / total * 100
    percentRange3 = len(range3) / total * 100
    percentRange4 = len(range4) / total * 100
    percentRange5 = len(range5) / total * 100
    percentRange6 = len(range6) / total * 100
    percentRange7 = len(range7) / total * 100
    percentRange8 = len(range8) / total * 100
    percentRange9 = len(range9) / total * 100
    print('======')
    print('Shopee:', percentRange1)
    print('Các sàn khác:', percentRange2)
    print('Amazon:', percentRange3)
    print('Sendo:', percentRange4)
    print('Lazada:', percentRange5)
    print('1688:', percentRange6)
    print('Facebook:', percentRange7)
    print('Alibaba:', percentRange8)
    print('TiktokShop:', percentRange9)
    print('======')
    data=[percentRange1,
          percentRange2,
          percentRange3,
          percentRange4,
          percentRange5,
          percentRange6,
          percentRange7,
          percentRange8,
          percentRange9,
          ]
    labels=['Shopee',
            'Các sàn khác',
            'Amazon',
            'Sendo',
            'Lazada',
            '1688',
            'Facebook',
            'Alibaba',
            'TiktokShop',
            ]
    veBieuDoTron(
        data=data,
        labels=labels,
    )
    veBieuDoCot(
        data=data,
        labels=labels
    )


def handleLevel():
    datas: List[str] = []

    range1: List[str] = []
    range2: List[str] = []

    for ele in level:
        if type(ele) is float: continue
        ele1 = ele.strip()

        datas.append(ele1)

        if ele1 == 'Không Hài Lòng':
            range1.append(ele1)
        if ele1 == 'Hài Lòng':
            range2.append(ele1)

    total = len(datas)
    percentRange1 = len(range1) / total * 100
    percentRange2 = len(range2) / total * 100
    print('======')
    print('Không hài lòng:', percentRange1)
    print('Hài lòng:', percentRange2)
    print('======')
    data=[percentRange1,
          percentRange2,
          ]
    labels=['Không hài lòng',
            'Hài lòng',
            ]
    veBieuDoTron(
        data=data,
        labels=labels,
    )
    veBieuDoCot(
        data=data,
        labels=labels
    )


def handleVote():
    datas: List[str] = []

    range1: List[str] = []
    range2: List[str] = []
    range3: List[str] = []
    range4: List[str] = []
    range5: List[str] = []
    for ele in vote:
        if type(ele) is float: continue
        ele1 = ele.strip()

        datas.append(ele1)

        if ele1 == '1Sao':
            range1.append(ele1)
        if ele1 == '2Sao':
            range2.append(ele1)
        if ele1 == '3Sao':
            range3.append(ele1)
        if ele1 == '4 Sao':
            range4.append(ele1)
        if ele1 == '5 Sao':
            range5.append(ele1)

    total = len(datas)
    percentRange1 = len(range1) / total * 100
    percentRange2 = len(range2) / total * 100
    percentRange3 = len(range3) / total * 100
    percentRange4 = len(range4) / total * 100
    percentRange5 = len(range5) / total * 100
    print('======')
    print('1 Sao:', percentRange1)
    print('2 Sao:', percentRange2)
    print('3 Sao:', percentRange2)
    print('4 Sao:', percentRange2)
    print('5 Sao:', percentRange2)
    print('======')
    data=[percentRange1,
          percentRange2,
          percentRange3,
          percentRange4,
          percentRange5,
          ]
    labels=['1 Sao',
            '2 Sao',
            '3 Sao',
            '4 Sao',
            '5 Sao',
            ]
    veBieuDoTron(
        data=data,
        labels=labels,
    )
    veBieuDoCot(
        data=data,
        labels=labels
    )


def handleReturnProduct():
    datas: List[str] = []

    range1: List[str] = []
    range2: List[str] = []

    for ele in returnProduct:
        if type(ele) is float: continue
        ele1 = ele.strip()

        datas.append(ele1)

        if ele1 == 'Sử Dụng':
            range1.append(ele1)
        if ele1 == 'Trả Hàng':
            range2.append(ele1)

    total = len(datas)
    percentRange1 = len(range1) / total * 100
    percentRange2 = len(range2) / total * 100
    print('======')
    print('Sử dụng:', percentRange1)
    print('Trả hàng:', percentRange2)
    print('======')
    data=[percentRange1,
          percentRange2,
          ]
    labels=['Sử dụng',
            'Trả hàng',
            ]
    veBieuDoTron(
        data=data,
        labels=labels,
    )
    veBieuDoCot(
        data=data,
        labels=labels
    )



# print(name)
# print(dateOfBirth)
# print(cardId)
# print(phone)
# print(salary)

if __name__ == '__main__':
    handleDateOfBirth(dateOfBirth)
    handleGender()
    handleSalary()
    handleBuyOften()
    handleShop()
    handleLevel()
    handleVote()
    handleReturnProduct()
