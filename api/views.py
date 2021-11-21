from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

import json
# Create your views here.

class CalculateChargeView(View):
    def post(self, request):
        data = json.loads(request.body)
        # user = request.user
        print(data)
        deer_name = data['deer_name']
        end_lat = data['end_lat']
        end_lng = data['end_lng']
        start_at = data['start_at']
        end_at = data['end_at']



        return JsonResponse({'message': 'SUCCESS', "deer_name": f'{deer_name}'}, status=200)

