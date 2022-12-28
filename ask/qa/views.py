from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question
from django.core.urlresolvers import reverse

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10

	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404

	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)

	return page, paginator

def index(request):
	qs = Question.objects.all()
	qs = qs.order_by('-added_at')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('index') + '?page='
	return render(request, 'index.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})	

def login(request):
	return HttpResponse('OK')

def signup(request):
	return HttpResponse('OK')

def question(request, pk):
	question = get_object_or_404(Question, id=pk)
	answers = question.answer_set.all()
	return render(request, 'question.html', {
		'question': question,
		'answers': answers,
	})	

def ask(request):
	return HttpResponse('OK')

def popular(request):
	qs = Question.objects.all()
	qs = qs.order_by('-rating')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('popular') + '?page='
	return render(request, 'popular.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})	

def new(request):
	return HttpResponse('OK')
