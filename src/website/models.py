from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	user = models.ForeignKey(User)
	posted = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=200)
	body = models.TextField()
	is_published = models.BooleanField(default=False)

	is_page = models.BooleanField(default=False)
	order = models.IntegerField(blank=True, null=True, help_text="Used to determine the order of display for Pages in navigation")

	def __unicode__(self):
		return u"{0}: {1}".format(self.title, self.user)

	def next_page_order(self):
		posts = Posts.objects.filter(is_page=True).order_by("-order")
		if posts:
			return posts[-1].order + 1
		else:
			return 0
