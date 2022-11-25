from MapBase import pre_Data, Map_Data, Merge_Data
import folium

# 파일명.csv 파일 전처리 후 사용 -> 학교명, 지원학과 항목만 

schoolname1 = './data/ahyeon.csv'
map1 = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData1 = pre_Data(schoolname1) # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
map1 = Map_Data(Merge_Data(SchoolData1), map1, "#00B8A9", "#00B8A9", 0.5, 1) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시여부(1, 0)) 
map1.save('./html/2023_ahyeon.html') # html 파일로 저장 / map.save('파일명.html')

schoolname2 = './data/enpyeong.csv'
map2 = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData2 = pre_Data(schoolname2)
map2 = Map_Data(Merge_Data(SchoolData2), map2, "#541212", "#541212", 0.5, 1)
map2.save('./html/2023_enpyeong.html') # html 파일로 저장 / map.save('파일명.html')

schoolname3 = './data/geumcheon.csv'
map3 = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData3 = pre_Data(schoolname3)
map3 = Map_Data(Merge_Data(SchoolData3), map3, "#3A6351", "#3A6351", 0.3, 1)
map3.save('./html/2023_geumcheon.html') # html 파일로 저장 / map.save('파일명.html')

schoolname4 = './data/seocho.csv'
map4 = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData4 = pre_Data(schoolname4)
map4 = Map_Data(Merge_Data(SchoolData4), map4, "#764AF1", "#764AF1", 0.3, 1)
map4.save('./html/2023_seocho.html') # html 파일로 저장 / map.save('파일명.html')

schoolname5 = './data/jongno.csv'
map5 = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정
SchoolData5 = pre_Data(schoolname5)
map5 = Map_Data(Merge_Data(SchoolData5), map5, "#FF1E1E", "#FF1E1E", 0.3, 1)
map5.save('./html/2023_jongno.html') # html 파일로 저장 / map.save('파일명.html')