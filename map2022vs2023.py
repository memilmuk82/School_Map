from MapBase import dept_Data, pre_Data, Map_Data, Merge_Data
import folium

map = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정

schoolname = 'jongno'
admission = '2023'
SchoolData = pre_Data(f'./data/{schoolname}.csv', schoolname, admission)
map = Map_Data(Merge_Data(SchoolData), map, "#FF1E1E", "#FF1E1E", 0.3, 1)

schoolname = 'jongno_2022'
admission = '2022'
SchoolData = pre_Data(f'./data/{schoolname}.csv', schoolname, admission)
map = Map_Data(Merge_Data(SchoolData), map, "#00B8A9", "#00B8A9", 0.3, 0)

map.save('./html/2022vs2023_map.html') # html 파일로 저장 / map.save('파일명.html')