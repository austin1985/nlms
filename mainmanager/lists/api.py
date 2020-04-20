from lists.models import *
from rest_framework import viewsets, permissions
from .serializers import *


# Lead Viewset (crud out of the box)
class ListsViewSet(viewsets.ModelViewSet):
    queryset = Lists.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ListsSerializer

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ListItemSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer

