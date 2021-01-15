from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReviewSerializer, MessageSerializer
from .models import Review, Message

# Create your views here.

@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": '/review-list',
        "Detail View": "/review-detail/<int:id>/",
        "Create": '/review-create/',
        "Update": '/review-update/<int:id>/',
        "Delete": '/review-delete/<int:id>/',
        "MessageList": '/message-list',
        "MessageCreate": '/message-create/'
    }
    return Response(api_urls)

@api_view(["GET"])
def reviewList(request):

    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def reviewDetail(request, id):

    reviews = Review.objects.get(id=id)
    serializer = ReviewSerializer(reviews, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def reviewCreate(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def reviewUpdate(request, id):
    review = Review.objects.get(id=id)
    serializer = ReviewSerializer(data=request.data, instance=review)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def reviewDelete(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return Response("item deleted")

@api_view(["GET"])
def messageList(request):

    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def messageCreate(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)