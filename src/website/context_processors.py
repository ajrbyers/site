from website import models

def navigation(request):
	"""
	This function injects the navigation into each request.

	:param request: the active request
	:return: dictionary containing a journal object under key 'journal' or None if this is a press site
	"""

	nav_items = models.Post.objects.filter(is_page=True, is_published=True).order_by("-order")
	print nav_items
	return {'nav': nav_items}