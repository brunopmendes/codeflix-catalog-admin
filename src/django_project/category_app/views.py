from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        return Response(status=HTTP_200_OK, data=[
            {
                "id": "87be2268-dcff-4f17-b1a6-421537d4ec98",
                "name": "Filme",
                "description": "Categoria para filmes",
                "is_active": True
            },
            {
                "id": "82552420-2c29-477b-91c6-265453c78dff",
                "name": "Série",
                "description": "Categoria para séries",
                "is_active": True
            }
        ])
