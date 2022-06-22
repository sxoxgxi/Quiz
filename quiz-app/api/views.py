from rest_framework.response import Response
from rest_framework.decorators import api_view

from base import models
from.serializers import QuestionsSerializer


@api_view(['GET'])
def getData(request):
    items = models.Questions.objects.all()
    serializer = QuestionsSerializer(items, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def addData(request):
#     serializer = QuestionsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
