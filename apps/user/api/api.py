from rest_framework.views import APIView
from apps.user.api.seralizers import UserSerializer
from apps.user.api.seralizers import User

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serilizer = UserSerializer(users, many=True)
        
        return Response(users_serilizer.data)




