from MapBase import dept_Data, pre_Data, Map_Data, Merge_Data
import folium

map = folium.Map(location=[37.55,126.98], zoom_start=12) # 기본맵 설정

#schoolname = 'ahyeon'
#deptname = '관광서비스'
#dept_Data(schoolname, deptname)  #특정 학과의 학교별 모집현황 파일 출력
#SchoolData = pre_Data(f'{schoolname}_{deptname}.csv', schoolname, deptname) # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
#map = Map_Data(Merge_Data(SchoolData), map, "#00B8A9", "#00B8A9", 0.5, 0) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시(표시:1, 미표시:0))

#schoolname = 'ahyeon'
#deptname = '연극영화-영화'
#dept_Data(schoolname, deptname)  #특정 학과의 학교별 모집현황 파일 출력
#SchoolData = pre_Data(f'{schoolname}_{deptname}.csv', schoolname, deptname) # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
#map = Map_Data(Merge_Data(SchoolData), map, "#00B8A9", "#00B8A9", 0.5, 0) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시(표시:1, 미표시:0))

#schoolname = 'enpyeong'
#deptname = '게임프로그래밍'
#dept_Data(schoolname, deptname)  #특정 학과의 학교별 모집현황 파일 출력
#SchoolData = pre_Data(f'{schoolname}_{deptname}.csv', schoolname, deptname) # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
#map = Map_Data(Merge_Data(SchoolData), map, "#541212", "#541212", 0.5, 0) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시(표시:1, 미표시:0)) 

#schoolname = 'geumcheon'
#deptname = '퍼스널트레이너'
#dept_Data(schoolname, deptname)  #특정 학과의 학교별 모집현황 파일 출력
#SchoolData = pre_Data(f'{schoolname}_{deptname}.csv', schoolname, deptname) # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
#map = Map_Data(Merge_Data(SchoolData), map, "#7900FF", "#7900FF", 0.5, 0) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시(표시:1, 미표시:0)) 

#schoolname = 'geumcheon'
#deptname = '제과제빵'
#dept_Data(schoolname, deptname)  #특정 학과의 학교별 모집현황 파일 출력
#SchoolData = pre_Data(f'{schoolname}_{deptname}.csv', schoolname, deptname) # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
#map = Map_Data(Merge_Data(SchoolData), map, "#7900FF", "#7900FF", 0.5, 0) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시(표시:1, 미표시:0)) 

schoolname = 'jongno'
deptname = '관광일본어과'
dept_Data(schoolname, deptname)  #특정 학과의 학교별 모집현황 파일 출력
SchoolData = pre_Data(f'./csv/{schoolname}_{deptname}.csv', schoolname, deptname) # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
map = Map_Data(Merge_Data(SchoolData), map, "#FF1E1E", "#FF1E1E", 0.3, 1) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시(표시:1, 미표시:0))

#schoolname = 'jongno'
#deptname = '항공서비스과'
#dept_Data(schoolname, deptname)  #특정 학과의 학교별 모집현황 파일 출력
#SchoolData = pre_Data(f'{schoolname}_{deptname}.csv', schoolname, deptname) # 학교 데이터 입력 / pre_Data('파일명.csv', '학교명', '정시 또는 추가')
#map = Map_Data(Merge_Data(SchoolData), map, "#FF1E1E", "#FF1E1E", 0.3, 1) # Map_Data(Merge_Data(SchoolData), map, '외곽선 색', '채우기 색', 투명도(0.0 ~ 1.0), 팝업표시(표시:1, 미표시:0)) 


map.save('./html/관광일본과_정시모집_지도.html') # html 파일로 저장 / map.save('파일명.html')