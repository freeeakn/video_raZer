from django.conf import settings
from graphene_django import DjangoObjectType
import graphene

from . import models


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile


class VideoType(DjangoObjectType):
    class Meta:
        model = models.Video


class Query(graphene.ObjectType):
    
    author_by_username = graphene.Field(AuthorType, username=graphene.String())

    def resolve_all_video(root, info, video):
        return (
            models.Post.objects.prefetch_related("video")
            .select_related("author")
            .all()
        )

    def resolve_author_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )


schema = graphene.Schema(query=Query)
