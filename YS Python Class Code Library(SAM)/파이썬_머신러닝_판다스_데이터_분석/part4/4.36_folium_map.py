# -*- coding: utf-8 -*-


# pip install folium
# 라이브러리 불러오기
import folium

lat = 7.29171
lng = 127.01241

loc = "연세IT미래교육원"

# 서울 지도 만들기
ysit_map = folium.Map(location=[37.29171,127.01241], zoom_start=12)

folium.Marker([37.29171,127.01241], popup=loc).add_to(ysit_map)


# 지도를 HTML 파일로 저장하기
ysit_map.save('./ysit.html')
