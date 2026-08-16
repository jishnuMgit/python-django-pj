from rest_framework import serializers
from blogs.models import Blogs,Comment




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'


class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Blogs
        fields='__all__'
