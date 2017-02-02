from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import QuestionForm
from .models import Question, Choice
# Create your views here.

def QuestionCreate(request):
    message = None
    if request.method == 'POST':
        ### Please do the form validation here
        ## if form.is_valid(), form save method etx
        ## Here I am doing the same view method insted of form save
        rg = request.POST.get
        if rg('question_text') and len(rg('choice'))>0:
            question = Question.objects.create(question_text=rg('question_text'))
            choices = request.POST.getlist('choice')
            for choice in choices:
                choice_q = Choice.objects.create(question=question, choice_text=choice)
            message = "Successfully added new questsion {0}".format(question.question_text)
        else:
            message = "Form Validation Error"
        form = QuestionForm()
    else:
        form = QuestionForm()
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     print(form.cleaned_data.get('question_text'))
    #     instance.save()

    context = { 'form': form,'message':message}
    return render(request,'polls/question_form.html',context)


def list(request):
	latest_question_list = Question.objects.all()
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/list.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
