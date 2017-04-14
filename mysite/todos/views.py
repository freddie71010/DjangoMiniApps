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
		print("REQUEST:",new_row_order)
		wip_new_row_order = new_row_order["wip[]"]
		future_new_row_order = new_row_order["future[]"]
		print("WIP:",wip_new_row_order)
		print("FUTURE:",future_new_row_order)
		
		# strips down row order to just an integer
		for i in range(len(wip_new_row_order)):
			wip_new_row_order[i]= int(wip_new_row_order[i].replace("item_",""))
		for i in range(len(future_new_row_order)):
			future_new_row_order[i]= int(future_new_row_order[i].replace("item_",""))

		todos = Todo.objects.all().order_by('task_row_order')
		for todo in todos:
			if todo.task_row_order in wip_new_row_order and todo.section !="wip":
				print("\tsection updated: WIP")
				todo.section = "wip"
			elif todo.task_row_order in future_new_row_order and todo.section !="future":
				print("\tsection updated: future")
				todo.section = "future"						
			else:
				print("\tskip")
			todo.save(update_fields=['section'])

		combo_new_row_order = []
		combo_new_row_order.extend(wip_new_row_order)
		combo_new_row_order.extend(future_new_row_order)
		print("COMBO:", combo_new_row_order)

		# iterates through todos and updates todo task_row_order with new value
		for todo in todos:
			print(todo,"\t\t",todo.task_row_order,end="")
			updated_row_num = combo_new_row_order.index(todo.task_row_order)
			print(" --> ", updated_row_num)
			todo.task_row_order = updated_row_num
			todo.save(update_fields=['task_row_order', 'section'])

		return render(request, self.template, {'todos': todos})