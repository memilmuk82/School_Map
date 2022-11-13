import pandas as pd
import json
from openpyxl import Workbook
from MapBase import request_geo, json_key

key = json_key('./vworld_key.json') # vworld key가 저장된 json파일명(경로 포함)

geo = pd.read_csv('seoul_school_address.csv') # 엑셀 파일 불러오기 및 정리

highschool_list = geo['학교명'].to_list()
address_list = geo['도로명주소'].to_list()

wb = Workbook()
sheet = wb.active

for num, value in enumerate(address_list):
    addr = value
    # print(addr)
    x, y = request_geo(addr, key) # API를 활용하여 주소를 좌표로 변환
    sheet.append([highschool_list[num], addr, x, y]) # 학교명, 도로명주소, x(경도),  y(위도)의 순서대로 엑셀에 저장

  
wb.save(r"School_Geo.xlsx")

geo = pd.read_excel('School_Geo.xlsx', engine='openpyxl', header=None) # School_Geo.xlsx파일은 헤더 부분이 없음, 엔진을 openpyxl로 지정

geo.columns=["학교명","도로명주소","경도","위도"] # 컬럼명을 헤더에 추가

geo.to_excel('School_Geo.xlsx') # 엑셀로 저장

geo.to_csv('School_Geo.csv', encoding='utf-8-sig') # csv로 저장