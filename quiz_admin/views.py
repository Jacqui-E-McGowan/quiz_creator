from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def login(request):
    errors = Admin.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        admin = Admin.objects.get(email=request.POST['login_email'])
        request.session['admin_id'] = admin.id
        request.session['greeting'] = admin.first_name
        return redirect('/dashboard')

def dashboard(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'quizzes': Quiz.objects.all(),
            'this_admin': Admin.objects.get(id=request.session['admin_id'])
        }
    return render(request, 'dashboard.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = Quiz.objects.quiz_validator(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/new')

    else:
        if 'image' in request.FILES:
            quiz = Quiz.objects.create(
            name = request.POST['name'],
            client = request.POST['client'],
            job_number = request.POST['job_number'],
            show_date = request.POST['show_date'],
            message = request.POST['message'],
            image = request.FILES['image'],
            created_by = request.POST['created_by'],
        )
        else:
            quiz = Quiz.objects.create(
            name = request.POST['name'],
            client = request.POST['client'],
            job_number = request.POST['job_number'],
            show_date = request.POST['show_date'],
            message = request.POST['message'],
            image = "",
            created_by = request.POST['created_by'],
        )

        return redirect(f'/dashboard/{quiz.id}/questions')

def questions(request, quiz_id):
    one_quiz = Quiz.objects.get(id=quiz_id)
    context = {
        'quiz': one_quiz,
        'num_questions': range(1,6),
    }
    return render(request, 'questions.html', context)

def add(request, quiz_id):
    associated_quiz = Quiz.objects.get(id=quiz_id)
    form_questions = request.POST.getlist('question_text')

    num = 1
    for q in form_questions:
        form_answers = request.POST.getlist('answer_'+str(num))

        Question.objects.create(
        question_text = q,
        answer_1 = form_answers[0],
        answer_2 = form_answers[1],
        answer_3 = form_answers[2],
        answer_4 = form_answers[3],
        quiz = associated_quiz,
        )
        num = num + 1

    return redirect('/dashboard')

def edit(request, quiz_id):
    one_quiz = Quiz.objects.get(id=quiz_id)
    context = {
        'quiz': one_quiz
    }
    return render(request, 'edit.html', context)

def update(request, quiz_id):
    errors = Quiz.objects.edit_validator(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect(f'/dashboard/{quiz.id}/edit')

    if request.method == 'POST':
        to_update = Quiz.objects.get(id=quiz_id)
        print(to_update)
        if request.FILES.get('image', False):
            to_update.image = request.FILES['image']
        else:
            to_update.image = to_update.image
        to_update.name = request.POST['name']
        to_update.client = request.POST['client']
        to_update.job_number = request.POST['job_number']
        to_update.show_date = request.POST['show_date']
        to_update.message = request.POST['message']
        to_update.save()

    return redirect(f'/dashboard/{quiz_id}/edit_questions')

def edit_questions(request, quiz_id):
    one_quiz = Quiz.objects.get(id=quiz_id)
    all_questions = Question.objects.filter(quiz_id=quiz_id)
    context = {
        'questions': all_questions,
        'num_questions': range(1,6),
        'quiz': one_quiz
    }
    return render(request, 'edit_questions.html', context)

def update_questions(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    # errors = Quiz.objects.edit_validator(request.POST)
    # if errors:
    #     for (key, value) in errors.items():
    #         messages.error(request, value)
    #     return redirect(f'/dashboard/{quiz.id}/edit_questions')

    to_updates = Question.objects.filter(quiz_id=quiz_id)
    for to_update in to_updates:
        print(to_update)
        to_update.question_text = request.POST['question_text_'+str(to_update.id)]
        to_update.answer_1 = request.POST['answer_'+str(to_update.id)+'_1']
        to_update.answer_2 = request.POST['answer_'+str(to_update.id)+'_2']
        to_update.answer_3 = request.POST['answer_'+str(to_update.id)+'_3']
        to_update.answer_4 = request.POST['answer_'+str(to_update.id)+'_4']
        to_update.save()

    return redirect(f'/dashboard')

def view(request, quiz_id):
    context = {
        'questions': Question.objects.all(),
        'quizes': Quiz.objects.all(),
        'quiz': Quiz.objects.get(id=quiz_id),
        'current_admin': Admin.objects.get(id=request.session['admin_id'])
    }

    return render(request, 'view.html', context)

def participants(request, quiz_id):
    one_quiz = Quiz.objects.get(id=quiz_id)
    context = {
        'quiz': one_quiz
    }
    return render(request, 'participants.html', context)

def delete(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    quiz.delete()

    return redirect('/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')



