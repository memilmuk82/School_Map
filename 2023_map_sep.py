from MapBase import pre_Data, Map_Data, Merge_Data
import folium

# 파일명.csv 파일 전처리 후 사용 -> 학교명, 지원학과 항목만 


map1 = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData1 = pre_Data('ahyeon.csv', '아현', '정시') # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
map1 = Map_Data(Merge_Data(SchoolData1), map1, "#00B8A9", "#00B8A9", 0.5, 1) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시여부(1, 0)) 
map1.save('2023_ahyeon.html') # html 파일로 저장 / map.save('파일명.html')

map2 = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData2 = pre_Data('enpyeong.csv', '은평', '정시')
map2 = Map_Data(Merge_Data(SchoolData2), map2, "#541212", "#541212", 0.5, 1)
map2.save('2023_enpyeong.html') # html 파일로 저장 / map.save('파일명.html')

map3 = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData3 = pre_Data('geumcheon.csv', '금천', '정시')
map3 = Map_Data(Merge_Data(SchoolData3), map3, "#7900FF", "#7900FF", 0.3, 1)
map3.save('2023_geumcheon.html') # html 파일로 저장 / map.save('파일명.html')

map4 = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData4 = pre_Data('jongno.csv', '종로', '정시')
map4 = Map_Data(Merge_Data(SchoolData4), map4, "#FF1E1E", "#FF1E1E", 0.3, 1)
map4.save('2023_jongno.html') # html 파일로 저장 / map.save('파일명.html')