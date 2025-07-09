# 검색어로 출력
# import requests
# import json

# # REST API 키 직접 입력
# REST_API_KEY = ''

# # 검색 키워드
# query = '스타벅스'

# # 중심 좌표 (서울 삼성동 쯤)
# x = 127.0221068
# y = 37.5912999

# # 반경 (미터 단위, 최대 10000)
# radius = 500

# # 요청 URL
# url = 'https://dapi.kakao.com/v2/local/search/keyword.json'

# # 요청 헤더
# headers = {
#     "Authorization": f"KakaoAK {REST_API_KEY}"
# }

# # 요청 파라미터
# params = {
#     "query": query,
#     "x": x,
#     "y": y,
#     "radius": radius
# }

# # API 호출
# response = requests.get(url, headers=headers, params=params)
# data = response.json()

# # JSON 예쁘게 출력
# print(json.dumps(data, indent=4, ensure_ascii=False))



#카테고리로 출력
from django.conf import settings
from django.http import JsonResponse
import requests
import json

from user.models import IndependencePlan

#중심좌표 반환
def get_region_center_coords(user):
    REST_API_KEY = settings.KAKAO_RESTAPI

    try:
        independanceplan = IndependencePlan.objects.get(user=user)
        area_si = independanceplan.area_si.strip()
        area_sgg = independanceplan.area_sgg.strip()
    except IndependencePlan.DoesNotExist:
        print(f"[❗] No IndependencePlan for {user}")
        return default_coords()

    # 예외적인 지역 처리 (세종시는 시/구 없이 단일시)
    if "세종" in area_si:
        query = "세종특별자치시"
    else:
        query = format_query(area_si, area_sgg)

    print(f"[🔍] 주소 검색 쿼리: {query}")

    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    headers = {
        "Authorization": f"KakaoAK {REST_API_KEY}"
    }
    params = {
        "query": query
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    print(f"[📦] Kakao 응답 for '{query}':", data)

    try:
        address_info = data['documents'][0]
        x = float(address_info['x'])  # longitude
        y = float(address_info['y'])  # latitude
        return x, y
    except (IndexError, KeyError):
        print(f"[❗] Failed to fetch coordinates for '{query}': list index out of range")
        print(f"[❗] 좌표를 불러올 수 없습니다 for user {user}")
        return default_coords()


#주소 형식 보정
def format_query(area_si, area_sgg):
    if not area_si.endswith(('시', '도')):
        area_si += '시'
    if not area_sgg.endswith(('구', '군')):
        area_sgg += '구'
    return f"{area_si} {area_sgg}"


def default_coords():
    return 126.9784147, 37.5666805