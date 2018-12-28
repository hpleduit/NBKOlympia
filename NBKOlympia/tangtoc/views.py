from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist

from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


# Global information about what is the current question being asked
currentQuestion = 0

# Create your views here.
@login_required(login_url="login")
def home(request):
    """
    The main page of the program, display all information needed
    """
    return render(request, template_name="tangtoc/home.html")


class NewQuestion(generic.CreateView):
    """
    Class-based view to handle creating a new question into database
    Using class-based view to have the default error handling
    """

    form_class = QuestionForm
    success_url = reverse_lazy("newQuestion")
    template_name = "baseForm.html"

    # Handle the get request to make sure only staff or admin can login to this page
    def get(self, request):
        user = request.user

        if user.is_staff or user.is_superuser:
            form = self.form_class()
            return render(request, template_name=self.template_name, context={"form": form})
        else:
            return HttpResponse("Bạn không được phép truy cập tính năng này, vui lòng liên hệ với thành viên quản lý hoặc admin")

class NewAnswer(generic.CreateView):
    """
    Class-based view to submit a new answer to the database
    """

    form_class = AnswerForm
    success_url = reverse_lazy("answer")
    template_name = "baseForm.html"

    # Handle the post method to inlcude question number and
    def post(self, request):
        global currentQuestion

        user = request.user 
        # Get the form data submitted by user
        formAnswer = AnswerForm(request.POST)
        # Create an answer instance but not yet saved
        answer = formAnswer.save(commit=False)
        answer.owner = user
        answer.question_number = currentQuestion

        # Save the answer
        answer.save()

        # Return a new page for the next question
        form = self.form_class()
        return render(request, template_name=self.template_name, context={"form": form})

@login_required(login_url="login")
def question(request, question_number):
    """
    View to handle displaying question. Receive a question number to notify the backend code
    """
    global currentQuestion

    user = request.user    
    # Check to make sure that only staff can access this link
    if not user.is_staff:
        return render(request, template_name="tangtoc/home.html", context={"message": "Xin lỗi, bạn không được phép truy cập"})
    else:
        # Get the question out of database
        try:
            question = Question.objects.get(question_number=question_number)
            # Change current question to the question being displayed
            currentQuestion = question_number
            return render(request, template_name="tangtoc/question.html", context={"question": question})
        except ObjectDoesNotExist:
            # Handle the does not exist exception
            return render(request, template_name="tangtoc/home.html", 
                                    context={"message": "Xin lỗi, bạn chưa có câu hỏi số {} trong cơ sở dữ liệu, vui lòng thêm câu hỏi.".format(question_number)})
        


    

