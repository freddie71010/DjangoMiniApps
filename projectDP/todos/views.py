from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
	template = "todos/index.html"
	
	def get(self, request):
		todos = Todo.objects.all()
		print(todos)
		return render(request, self.template, {'todos': todos})

	def post(self, request):
		pass