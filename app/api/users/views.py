from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api.users.serializers import UserSerializer


class UserLoginView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.POST)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request=request,
            username=serializer.validated_data["user"],
            password=serializer.validated_data["password"],
        )
        if user is not None:
            login(request, user)
            return Response()
        return Response(status=status.HTTP_400_BAD_REQUEST)




