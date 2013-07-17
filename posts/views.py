# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from posts.models import Post

def index(request):
	posts = Post.objects.order_by('-pub_date')[:5]
	#output = ', '.join([p.title for p in posts])
	#return HttpResponse(output)
	template =loader.get_template('posts/index.html')
	context = RequestContext(request, {
		'posts' : posts,
	})
	return HttpResponse(template.render(context))


