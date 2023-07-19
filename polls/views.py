from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .models import Question, Choice

# Create your views here.




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    question_for_template = list(Question.objects.all())
    context = {
        'Latest_Question_List':latest_question_list,
        'question_for_template':question_for_template,
        }

    return render(request,'polls/index.html',context)


def detail(request,pk):
    try:
        question = Question.objects.get(pk = pk)
        context = {"question":question}
    except Question.DoesNotExist:
        raise Http404("Question doesnot exist.")
    return render(request, "polls/detail.html",context)

#### demonstrating the use of getobjector404

'''def detail(request, pk):
    question = get_object_or_404(Question, pk = pk)
    context = {"question":question}
    return render(request, "polls/detail.html",context)'''


def results(request,pk):
    question = get_object_or_404(Question, pk = pk)
    context = {"question":question}
    return render(request, "polls/results.html",context)


def vote(request,pk):
    question = get_object_or_404(Question, pk = pk)
    context = {
        "question" : question,
        "error_message" : "Please select a choice."
    }
    
    try:
        ## request.POST is a dictionary like object that help to retrieve the data using the key as choice
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return HttpResponse(f"You have successfully voted {selected_choice.choice_text} in the question of id : {question.id} of\n{question}.")
        # return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        
        return redirect("polls:results",pk = question.id)

    
