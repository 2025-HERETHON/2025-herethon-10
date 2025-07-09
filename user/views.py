from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, IndependencePlanForm
from django.http import HttpResponse
import requests
import copy
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

#서비스아이디, 보안키로 어세스토큰 받아오기
def get_token():

    url = 'https://sgisapi.kostat.go.kr/OpenAPI3/auth/authentication.json'  

    params = {
        'consumer_key': settings.CONSUMER_KEY,
        'consumer_secret': settings.CONSUMER_SECRET
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        result = response.json()  # 응답을 JSON으로 파싱
        
        access_token = result.get('result', {}).get('accessToken')

        return access_token
    
    except requests.exceptions.RequestException as e:
        return None

# SGIS 공통 API 호출 함수
def call_sgis_api(params=None):
    base_url = "https://sgisapi.kostat.go.kr/OpenAPI3/addr/stage.json"

    if params is None:
        params = {}
    else:
        params = copy.deepcopy(params)

    access_token = get_token()
    if not access_token:
        return {"error": "Access token을 가져오지 못했습니다."}

    params['accessToken'] = access_token

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # 에러 코드 검사
        if data.get('errCd') != 0:
            print(f"SGIS API 에러 발생: {data.get('errMsg', '')}")
            return {"error": data.get('errMsg', '알 수 없는 오류')}

        return data

    except requests.exceptions.RequestException as e:
        print("SGIS 호출 오류:", e)
        return {"error": str(e)}


# 시/도 가져오기
def get_sido(request):
    data = call_sgis_api({})
    return JsonResponse(data)


# 시/군/구 가져오기
def get_sigungu(request):
    sido_code = request.GET.get('sido_code')
    if not sido_code:
        return JsonResponse({"error": "sido_code is required"}, status=400)
    
    data = call_sgis_api({'cd': sido_code})
    # print(f"시/군/구 데이터 for sido_code={sido_code}: ", data)
    return JsonResponse(data)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import IndependencePlanForm

@login_required
def signup_view(request):
    # 만약 이미 독립계획 정보가 있는 유저라면 바로 home으로 보냄
    if hasattr(request.user, 'independenceplan'):
        return redirect('/home/')

    if request.method == 'POST':
        form = IndependencePlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect('/home/')
    else:
        form = IndependencePlanForm()

    return render(request, 'test_signup.html', {'plan_form': form})


