from django.http import HttpResponse
from django.shortcuts import render
import requests, urllib, json

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def get_food_info(request):
    if request.method == "GET":
        text = request.POST.get('inputText')
        # pub_api_info 가져오기 
        food_info = get_pub_api_info(text)
        
        # 데이터 가공 
        
        food_name = "" 
        if food_info is not None:
            food_name = food_info['foodNm']
        return render(request, 'view_list.html', {'food_info': food_info.items(), 'food_name': food_name})
    return render(request, 'view_list.html', {'user_input': 'POST 아님'})

def get_pub_api_info(input_text):
    url = 'http://api.data.go.kr/openapi/tn_pubr_public_nutri_food_info_api'
    api_key = '37bcdfe5ecd2ae75c4bab7796dff845762fbf4ff1f6c338629ba0980431f8999'
    params = {'serviceKey' : api_key, 'pageNo' : '1', 'numOfRows' : '100', 'type' : 'json'}

    response = requests.get(url, params=params)
    
    # json.loads로 json 데이터를 dict로 변경 
    json_data = json.loads(response.text)
    
    # body > item 들을 가져온다. items = list() 형태
    items = json_data['response']['body']['items']
    
    # loop을 돌면서 input_text와 동일한 정보의 데이터를 가져온다. 
    # # 제공할 정보 : 음식이름(foodNm), 음식분류(foddLv3Nm)
    result = None
    for item in items:
        food_name = item['foodNm']
        if input_text == food_name:
            result = item
            break
        
    return result