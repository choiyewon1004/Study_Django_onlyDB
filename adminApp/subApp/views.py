from django.http import HttpResponse
from django.shortcuts import render
import csv
from .models import *
from django.db.models import Q
from datetime import datetime

def clothes_insert(request):
    path = 'C:/Users/esthe/PycharmProjects/clother/adminApp/subApp/static/csv/final_clothes_csv.csv'
    file = open(path, 'r',encoding='UTF8')
    reader2 = csv.reader(file)

    list = []

    for row in reader2:
        list.append(CLOTHES_INFO(
            CLOTHES_IDX=row[0], CLOTHES_MON=row[1], CLOTHES_PNG=row[2], CLOTHES_LOC=row[3],
            CLOTHES_SHIRT_SHORT=row[4], CLOTHES_SHIRT_LONG=row[5], CLOTHES_SHIRT_SWEAT=row[6], CLOTHES_SWEATER=row[7], CLOTHES_SHIRT=row[8],
            CLOTHES_BLOUS=row[9], CLOTHES_ONEPICE=row[10], CLOTHES_NEET=row[11], CLOTHES_SHIRT_POLO=row[12], CLOTHES_KARDIGUN=row[13],
            CLOTHES_JUMPER=row[14], CLOTHES_JACKET=row[15], CLOTHES_COAT=row[16], CLOTHES_PADDING=row[17], CLOTHES_JEANS=row[18],
            CLOTHES_PANTS_WINTER=row[19],  CLOTHES_PANTS_SUMMER=row[20], CLOTHES_SKERT=row[21], CLOTHES_PANTS_CAGO=row[22], CLOTHES_SHOOSE_GUDU=row[23],
            CLOTHES_SHOOSE_RUNNING=row[24], CLOTHES_SHOOSE_SNIKERS=row[25], CLOTHES_SHOOSE_SANDAL=row[26], CLOTHES_SHOOSE_WAKER=row[27],
            CLOTHES_SHOOSE_BOOTS=row[28], CLOTHES_1=row[29], CLOTHES_2=row[30], CLOTHES_3=row[31],CLOTHES_4=row[32])
        )
    print(list)

    CLOTHES_INFO.objects.bulk_create(list)
    pass

def user_insert(request):
    path = 'C:/Users/esthe/PycharmProjects/clother/adminApp/subApp/static/csv/user.csv'
    file = open(path, 'r',encoding='UTF8')
    reader2 = csv.reader(file)

    list = []

    for row in reader2:
        list.append(user_tbl(
            user_id = row[1], user_pwd = row[2], user_name = row[1])
        )
    print(list)

    user_tbl.objects.bulk_create(list)
    pass


def test(request):
    # 데이터 삽입 처음시만 데이터 저장용
    # clothes_insert(request)
    # user_insert(request)

    # 패딩 입은 사람만 출력
    selects = CLOTHES_INFO.objects.filter(CLOTHES_PADDING=1)

    # 데이터 전체 출력
    #selects = CLOTHES_INFO.objects.all()
    context = {'select_list': selects}

    return render(request, 'subApp/test.html', context)


def font_test(request):
    return render(request, 'subApp/font_test.html')

def button_test(request):
    return render(request, 'subApp/button_test.html')

def search_bar(request):
    return render(request, 'subApp/index.html')