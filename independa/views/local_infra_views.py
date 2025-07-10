from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.conf import settings
import requests
from independa.models import SavedPlace
from independa.utils.restapi_search import get_region_center_coords
from user.models import IndependencePlan

from django.shortcuts import render
from django.conf import settings

def local_infra_view(request):
    x, y = get_region_center_coords(request.user)

    if not x or not y:
        print(f"[❗] 좌표를 불러올 수 없습니다 for user {request.user}")
        context = {
            'error': "주소 기반 좌표를 찾을 수 없습니다.",
            'myjskey': settings.MYJSKEY
        }
        return render(request, 'test_local_infra_error.html', context)  # 에러 템플릿 따로 둘 수도 있음

    print(f"[📍] 중심좌표: x={x}, y={y}")

    context = {
        'x': x,
        'y': y,
        'myjskey': settings.MYJSKEY,
        'rest_api': settings.KAKAO_RESTAPI,
    }
    return render(request, 'test_local_infra.html', context)


from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def save_place(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = request.user
        
        if SavedPlace.objects.filter(user=user, kakao_id=data['kakao_id']).exists():
            return JsonResponse({"success": False, "message": "이미 저장됨"})
        
        SavedPlace.objects.create(
            user=user,
            kakao_id=data["kakao_id"],
            category_group_code=data["category_group_code"],
            place_name=data["place_name"],
            place_url=data["place_url"],
            road_address_name=data["road_address_name"],
            x=data["x"],
            y=data["y"]
        )
        return JsonResponse({"success": True})
    
    
from django.views.decorators.http import require_GET

@require_GET
def category_search_map(request, category_group_code):
    user = request.user
    REST_API_KEY = settings.KAKAO_RESTAPI

    # 좌표 처리
    x = request.GET.get("x")
    y = request.GET.get("y")
    
    if x and y:
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            return JsonResponse({"places": [], "error": "Invalid coordinates"}, status=400)
    else:
        x, y = get_region_center_coords(user)

    page = request.GET.get("page", 1)

    url = 'https://dapi.kakao.com/v2/local/search/category.json'

    headers = {
        "Authorization": f"KakaoAK {REST_API_KEY}"
    }

    params = {
        "category_group_code": category_group_code,
        "x": x,
        "y": y,
        "sort": "distance",
        "radius": 20000,
        "page": page
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    places = data.get('documents', [])

    return JsonResponse({'places': places})

# 검색어로 출력
import requests
import json

def keyword_search_map(request):
    query = request.GET.get('query', '')
    page = int(request.GET.get('page', '1'))
    x = request.GET.get('x')
    y = request.GET.get('y')

    if not query:
        return JsonResponse({'places': []})

    REST_API_KEY = settings.KAKAO_RESTAPI
    headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}

    params = {
        'query': query,
        'page': page,
        'x': x,
        'y': y,
        'radius': 2000,
        'size': 15,
        'sort': 'distance',
    }

    response = requests.get("https://dapi.kakao.com/v2/local/search/keyword.json", headers=headers, params=params)
    data = response.json()

    places = []
    for doc in data.get('documents', []):
        places.append({
            'id': doc['id'],
            'category_group_code': doc.get('category_group_code', ''),
            'place_name': doc['place_name'],
            'place_url': doc['place_url'],
            'road_address_name': doc['road_address_name'],
            'address_name': doc['address_name'],
            'x': doc['x'],
            'y': doc['y'],
        })

    return JsonResponse({'places': places})