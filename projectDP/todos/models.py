from django.db import models

class Todo(models.Model):
	task = models.CharField(max_length=200)
	task_row_order = models.IntegerField()

	def __str__(self):
		return self.task