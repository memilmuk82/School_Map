from MapBase import pre_Data, Map_Data, Merge_Data
import folium

# 파일명.csv 파일 전처리 후 사용 -> 학교명, 지원학과 항목만 
map = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정

schoolname = './data/ahyeon.csv' 
SchoolData = pre_Data(schoolname) # 학교별 합격자 수 정리 
map = Map_Data(Merge_Data(SchoolData), map, "#00B8A9", "#00B8A9", 0.5, 0) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시(표시:1, 미표시:0)) 

schoolname = './data/enpyeong.csv' 
SchoolData = pre_Data(schoolname)
map = Map_Data(Merge_Data(SchoolData), map, "#541212", "#541212", 0.5, 0)

schoolname = './data/geumcheon.csv' 
SchoolData = pre_Data(schoolname)
map = Map_Data(Merge_Data(SchoolData), map, "#3A6351", "#3A6351", 0.5, 0)

schoolname = './data/seocho.csv' 
SchoolData = pre_Data(schoolname)
map = Map_Data(Merge_Data(SchoolData), map, "#764AF1", "#764AF1", 0.5, 0)

schoolname = './data/jongno.csv'
SchoolData = pre_Data(schoolname)
map = Map_Data(Merge_Data(SchoolData), map, "#FF1E1E", "#FF1E1E", 0.3, 1)

map.save('./html/2023map.html') # html 파일로 저장 / map.save('파일명.html')