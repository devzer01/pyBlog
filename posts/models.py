from django.db import models

#lets create a custom type for mediumtext

class MediumText(models.Field):
	def db_type(self, connection):
		return 'mediumtext'

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	article = MediumText()
	pub_date = models.DateTimeField('publish date')

class Comment(models.Model):
	post = models.ForeignKey(Post)
	comment = models.CharField(max_length=200)
	created_date = models.DateTimeField('created date')
	
