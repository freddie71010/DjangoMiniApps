from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
	template = "todos/index.html"
	
	def get(self, request):
		todos = Todo.objects.all().order_by('task_row_order')
		print(todos)
		return render(request, self.template, {'todos': todos})

	def post(self, request):
		new_row_order = dict(request.POST)
		new_row_order = new_row_order["sorted[]"]
		
		# strips down row order to just an integer
		for i in range(len(new_row_order)):
			new_row_order[i]= int(new_row_order[i].replace("item_",""))
		
		todos = Todo.objects.all().order_by('task_row_order')
		i = 0
		# iterates through todos and updates todo task_row_order with new value
		for todo in todos:
			updated_row_num = new_row_order.index(todo.task_row_order)
			print(todo,end="\t\t")
			print("updated_row_num: ", updated_row_num)
			todo.task_row_order = updated_row_num
			todo.save(update_fields=['task_row_order'])
			i += 1

		return render(request, self.template, {'todos': todos})