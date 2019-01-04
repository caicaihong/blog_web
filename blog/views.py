from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from blog.models import BlogArticles
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
import json
# Create your views here.


def blog_title(request):
	response = {}
	blog_list = []
	print(request.method)
	data = json.loads(bytes.decode(request.body))

	print(data)
	user = User.objects.get(username=data['username'])
	print(user.username)
	blogs = BlogArticles.objects.all()
	for blog in blogs:
		blog_list.append(blog.title)
	print(blog_list)
	response['blog'] = [blog.title for blog in blogs]
	response['msg'] = 'success'
	return JsonResponse(response)


