from django.http import HttpResponse


def index(request):
    return HttpResponse(
    "<h1>TEST TEST TEST Hello, world.</h1> You're at the polls index.<br>"
    "<a href='https://www.w3schools.com/'>Visit W3Schools.com!</a><br>"
    '<button type="button">Click Me!</button>'
    )

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)