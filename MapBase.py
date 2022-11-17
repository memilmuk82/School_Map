import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook
import folium
import requests
import json

def json_key(json_name):
    client = None
    with open(json_name,"r") as clientJson :
        client = json.load(clientJson)
    return client["key"] 

def request_geo(road, primary_key): # 주소를 x, y좌표로 반환해주는 함수 -> API에 접속하여 x, y 부분만 분리하여 반환
    # VWORLD API 접속 관련 내용 
    url= 'http://api.vworld.kr/req/address?'
    params = 'service=address&request=getcoord&vision=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
    road_type = 'ROAD' #도로명 주소
    road_type2 = 'PARCEL' #지번 주소
    address = '&address='
    keys = '&key='
    primary_key = primary_key # 발급 받은 인증키 입력
    page = requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data = page.json()
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x, y
    else:
        x = 0
        y = 0
        return x, y

def pre_Data(FileName):
    df = pd.read_csv(FileName)
    Enrollment=pd.DataFrame()
    Freshman=df['학교명'].value_counts()
    Enrollment['학교명'] = Freshman.index
    Enrollment['학생수'] = Freshman.values # 시리즈를 데이터프레임으로 변환
    Enrollment = Enrollment.sort_values('학교명').reset_index(drop=True) # 학교명으로 정렬
    return Enrollment

def dept_Data(FileName, DeptName): #특정 학과의 학교별 모집현황 파일 출력
    df = pd.read_csv(f'{FileName}.csv')
    department = df.loc[(df['지원학과'] == DeptName)]
    department = department.sort_values('학교명').reset_index(drop=True) # 학교명으로 정렬
    department.to_csv(f'./csv/{FileName}_{DeptName}.csv')
    if ( __name__ == "__main__" ) :
        print(department.head())
    return department

def Merge_Data(SchoolData):
    map = pd.read_excel('School_Geo.xlsx') # 학교별 주소, 위치, 위도, 경도를 map에 저장(서울시 고등학교 기본정보 활용하여 엑셀파일에 학교명과 주소, 위치만 남기고 삭제한 파일)
    SchoolData = pd.merge(map, SchoolData, how='left', left_on='학교명', right_on='학교명')
    SchoolData = SchoolData.dropna(axis=0).sort_values('학교명').reset_index(drop=True)
    # '학교명', '학생수', '도로명주소', 'x', 'y' 값을 각각 리스트 형태로 가져옴
    return SchoolData

def Map_Data(SchoolData, map, color, fill_color,fill_opacity, number):
    name_list = SchoolData['학교명'].to_list() # 학교명
    student_list = SchoolData['학생수'].to_list() # 학생수
    addr_list = SchoolData['도로명주소'].to_list() # 도로명주소
    position_x_list = SchoolData['경도'].to_list() # 경도
    position_y_list = SchoolData['위도'].to_list() # 위도
    for i in range(len(name_list)):
        if position_x_list[i] != 0:
            if number == 0:
                marker1 = folium.CircleMarker([position_y_list[i], position_x_list[i]], radius=student_list[i]+5, 
                            popup=name_list[i], color=color, fill=True, fill_color=fill_color,
                                fill_opacity=fill_opacity, tooltip=name_list[i]) # 마커 지정 -> 위도, 경도 / 팝업 -> 학교명 / 아이콘 지정        
                marker1.add_to(map) # 마커 추가
            else:
                marker1 = folium.CircleMarker([position_y_list[i], position_x_list[i]], radius=student_list[i]+5, 
                            popup=name_list[i]+str(int(student_list[i])), color=color, fill=True, fill_color=fill_color,
                            fill_opacity=fill_opacity, tooltip=name_list[i]+str(int(student_list[i]))) # 마커 지정 -> 위도, 경도 / 팝업 -> 학교명 / 아이콘 지정        
                marker1.add_to(map) # 마커 추가
    return map

