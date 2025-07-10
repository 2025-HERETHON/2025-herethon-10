import json
from django.conf import settings
from django.shortcuts import render
from independa.models import SavedPlace
from independa.utils.restapi_search import get_region_center_coords


def scrap_infra_view(request):
    x, y = get_region_center_coords(request.user)

    if not x or not y:
        print(f"[❗] 좌표를 불러올 수 없습니다 for user {request.user}")
        context = {
            'error': "주소 기반 좌표를 찾을 수 없습니다.",
            'myjskey': settings.MYJSKEY
        }
        return render(request, 'test_local_infra_error.html', context)  # 에러 템플릿 따로 둘 수도 있음

    print(f"[📍] 중심좌표: x={x}, y={y}")

    saved_places = SavedPlace.objects.filter(user=request.user)
    
    place_list = [
        {
            "id": p.kakao_id,
            "category_group_code": p.category_group_code,
            "place_name": p.place_name,
            "place_url": p.place_url,
            "road_address_name": p.road_address_name,
            "address_name": p.road_address_name,  # 백업용
            "x": p.x,
            "y": p.y
        }
        for p in saved_places
    ]
    print(f"[📦] 저장된 장소 개수: {saved_places.count()}")
    context = {
        'x': x,
        'y': y,
        'myjskey': settings.MYJSKEY,
        'rest_api': settings.KAKAO_RESTAPI,
        'saved_place': json.dumps(place_list, ensure_ascii=False),
        'saved_places' : saved_places
    }
    return render(request, 'test_scrap_infra.html', context)

from django.views.decorators.http import require_POST
from django.http import JsonResponse
from independa.models import SavedPlace  # 모델 이름에 맞게 수정

@require_POST
def delete_place_view(request, place_id):
    try:
        place = SavedPlace.objects.get(kakao_id=place_id, user=request.user)
        place.delete()
        return JsonResponse({'success': True})
    except SavedPlace.DoesNotExist:
        return JsonResponse({'success': False, 'error': '존재하지 않는 장소'}, status=404)
    
    
def filter_saved_places_view(request):
    user = request.user
    category = request.GET.get("category")
    
    places = SavedPlace.objects.filter(user=user, category_group_code=category).values(
        "id", "place_name", "place_url", "road_address_name", "x", "y", "category_group_code"
    )

    return JsonResponse({"places": list(places)})