from django.views import View
from django.http import JsonResponse
from .charging_policies.dto import UserDTO
import json
from datetime import datetime
from api.cost_calculator import CostCalculator
from .models import  User, Deer

class CalculateChargeView(View):

    def post(self, request):
        data = json.loads(request.body)

        userdto = UserDTO()
        user = User.objects.get(name= data["user_name"])
        deer =  Deer.objects.get(name=data['deer_name'])
        userdto.user_id = user.id
        userdto.use_deer = deer
        userdto.use_end_lat = data['end_lat']
        userdto.use_end_lng = data['end_lng']
        userdto.use_start_at = datetime.strptime(data['start_at'], '%Y-%m-%d %H:%M:%S')
        userdto.use_end_at = datetime.strptime(data['end_at'], '%Y-%m-%d %H:%M:%S')


        costCalculator = CostCalculator(userdto)

        policies_and_charge =costCalculator.calculate()

        return JsonResponse({'message': 'SUCCESS', 'charge_cost':f'{policies_and_charge[-1]}, "요금 근거: f{policies_and_charge[:-1]}'}, status=200)




