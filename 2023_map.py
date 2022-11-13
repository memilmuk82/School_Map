from MapBase import pre_Data, Map_Data, Merge_Data
import folium

# 파일명.csv 파일 전처리 후 사용 -> 학교명, 지원학과 항목만 
map = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData = pre_Data('ahyeon.csv', '아현', '정시') # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
map = Map_Data(Merge_Data(SchoolData), map, "#00B8A9", "#00B8A9", 0.5, 0) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시(표시:1, 미표시:0)) 

SchoolData = pre_Data('enpyeong.csv', '은평', '정시')
map = Map_Data(Merge_Data(SchoolData), map, "#541212", "#541212", 0.5, 0)

SchoolData = pre_Data('geumcheon.csv', '금천', '정시')
map = Map_Data(Merge_Data(SchoolData), map, "#7900FF", "#7900FF", 0.3, 1)

SchoolData = pre_Data('jongno.csv', '종로', '정시')
map = Map_Data(Merge_Data(SchoolData), map, "#FF1E1E", "#FF1E1E", 0.3, 1)

map.save('2023map.html') # html 파일로 저장 / map.save('파일명.html')