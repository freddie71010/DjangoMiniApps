from django.db import models


SECTIONS =  (
		('wip', 'wip'),
		('completed', 'completed'),
		('future', 'future'),
	)

class Todo(models.Model):
	task = models.CharField(max_length=200)
	task_row_order = models.IntegerField()
	section = models.CharField(default="Blank", max_length=100, choices=SECTIONS)
	
	def __str__(self):
		return self.task

	