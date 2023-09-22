from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 서버에서 발생한 에러를 보안상 이슈로 클라이언트로 보내는것은 좋지 않음 / 개발 단게에서 error를 보내고 해결되면 삭제
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
