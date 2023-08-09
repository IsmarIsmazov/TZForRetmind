from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer,LoginSerializer
from .tokens import create_jwt_pair_for_user
from .permissions import IsUnregistered

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [IsUnregistered]

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [IsUnregistered]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data["email"],
                                password=serializer.validated_data["password"])

            if user is not None:
                tokens = create_jwt_pair_for_user(user)

                response = {"message": "Login Successful", "tokens": tokens}
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                return Response(data={"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)