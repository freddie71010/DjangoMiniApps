from django.db import models


SECTIONS =  (
		('WIP', 'WIP'),
		('Completed', 'Completed'),
		('Future', 'Future'),
	)

class Todo(models.Model):
	task = models.CharField(max_length=200)
	task_row_order = models.IntegerField()
	section = models.CharField(max_length=10, choices=SECTIONS)
	
	def __str__(self):
		return self.task

	