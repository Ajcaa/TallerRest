
#Basado en un modelo
""" from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TodoSerializer
 """


#NO basado en un modelo
'''
from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TestTodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TestTodoSerializer
'''




#Taller vistas
from .models import Todo
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializer

#Taller JWT
from rest_framework.permissions import IsAuthenticated
'''
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TodoSerializer
'''

class DeleteAllTodo(APIView):
    def delete(self, request):
        # Elimina todos los registros
        Todo.objects.all().delete()
        # Retorna un status code de 204 indicando que no existe contenido dentro de nuestra base de datos
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetAllTodo(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many = True)
        return Response(serializer.data)




class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer