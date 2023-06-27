from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Answer
from .models import UserAnswer
from django.db.models import Count


class QuizView(View):
    def get(self, request):
        user_id = request.session.get('user_id')
        if not user_id:
            user_id = hash(request.session.session_key)
            request.session['user_id'] = user_id
        user_answers = UserAnswer.objects.filter(user_id=user_id)
        answered_question_ids = user_answers.values_list('answer__question_id', flat=True)

        if len(answered_question_ids) == 8:
            return redirect('result')

        unanswered_questions = Question.objects.exclude(id__in=answered_question_ids)
        question = unanswered_questions.first()
        answers = Answer.objects.filter(question=question)

        context = {
            'question': question,
            'answers': answers,
        }
        return render(request, 'quiz.html', context=context)

    def post(self, request):
        user_id = request.session.get('user_id')
        answer_id = request.POST.get('answer')

        if user_id and answer_id:
            user_answer = UserAnswer(user_id=user_id, answer_id=answer_id)
            user_answer.save()

        return redirect('quiz')

class ResultView(View):
    def get(self, request):
        user_id = request.session.get('user_id')
        user_answers = UserAnswer.objects.filter(user_id=user_id)
        answer_counts = user_answers.values('answer__personality_type').annotate(count=Count('answer__personality_type')).order_by('-count')

        result = answer_counts.first()

        context = {
            'result': result,
        }
        return render(request, 'result.html', context=context)


class ResetAnswersView(View):
    def get(self, request):
        user_id = request.session.get('user_id')
        if user_id:
            UserAnswer.objects.filter(user_id=user_id).delete()
            del request.session['user_id']
        return redirect('quiz')