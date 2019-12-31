from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Article
# Create your views here.

class ArticleListView(ListView):
	model = Article
	template_name = 'home.html'

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'detail.html'
	"""docstring for ArticleDetailView"DetailViewf 
	model = Article
	template_name = 'detail.html'__init__(self, arg):
		super(ArticleDetailView,DetailView._
		model = Article
		template_name = 'detail.html'_init__()
		self.arg = arg"""