from .models import RandomQuotes
from rest_framework.permissions import AllowAny
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class RandomQuotesViewSet(APIView):
    permission_classes = [AllowAny]
    api_url = 'https://favqs.com/api/qotd'

    def post(self, request):
        response = requests.get(self.api_url)
        info = response.json()

        user_data = info['quote']
        user_model_data = {
            'author': user_data['author'],
            'body': user_data['body'],

        }

        random_user = RandomQuotes.objects.create(**user_model_data)

        return Response({'status': 'success'})




