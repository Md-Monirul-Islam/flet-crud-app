from rest_framework.viewsets import ModelViewSet
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class ItemViewSet(ModelViewSet):
    """
    ViewSet for performing CRUD operations on Items.
    """
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]  # Allow frontend requests

    def update(self, request, *args, **kwargs):
        """
        Update an existing item.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an item with proper error handling.
        """
        instance = self.get_object()
        try:
            instance.delete()
            return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
