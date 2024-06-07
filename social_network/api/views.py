from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from .models import CustomUser, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer, UserSignupSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSearchView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if '@' in query:
            return CustomUser.objects.filter(email__iexact=query)
        return CustomUser.objects.filter(username__icontains=query)


class FriendRequestView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        from_user = request.user
        to_user_id = request.data.get('to_user_id')
        try:
            to_user = CustomUser.objects.get(id=to_user_id)
            FriendRequest.objects.create(from_user=from_user, to_user=to_user, status='pending')
            return Response({"message": "Friend request sent"}, status=status.HTTP_201_CREATED)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        received_requests = FriendRequest.objects.filter(to_user=request.user, status='pending')
        serializer = FriendRequestSerializer(received_requests, many=True)
        return Response(serializer.data)


class FriendListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friends = CustomUser.objects.filter(
            sent_requests__to_user=request.user, 
            sent_requests__status='accepted'
        )
        serializer = UserSerializer(friends, many=True)
        return Response(serializer.data)
