from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question
from django.core.urlresolvers import reverse
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import login, logout

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
	page, paginator = paginate(request, Question.objects.new())
	paginator.baseurl = reverse('index') + '?page='
	return render(request, 'index.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})	

def question(request, pk):
	question = get_object_or_404(Question, id=pk)
	answers = question.answer_set.all()
	form = AnswerForm(initial={'question': str(pk)})
	return render(request, 'question.html', {
		'question': question,
		'answers': answers,
		'form': form,
	})	

def ask(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			if request.user.is_anonymous():
				return HttpResponseRedirect('/login')

			form.user = request.user
			question = form.save()
			url = reverse('question', args=[question.id])
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'asked_question.html', {
		'form': form
	})

def answer(request):
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			if request.user.is_anonymous():
				return HttpResponseRedirect('/login')

			form.user = request.user
			answer = form.save()
			url = reverse('question', args=[answer.question.id])
			return HttpResponseRedirect(url)
	return HttpResponseRedirect('/')


def popular(request):
	page, paginator = paginate(request, Question.objects.popular())
	paginator.baseurl = reverse('popular') + '?page='
	return render(request, 'popular.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})	

def new(request):
	return HttpResponse('OK')

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/')

	form = SignupForm()
	return render(request, 'signup.html', {
		'form': form
	})

def login_user(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.save()
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/')

	form = LoginForm()
	return render(request, 'login.html', {
		'form': form
	})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')
