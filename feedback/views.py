from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from .forms import FeedbackForm



class FeedbackView(View):
    """Форма обратной связи"""
    def get(self, request):
        form = FeedbackForm
        return render(request, 'feedback/feedback.html', {'form': form})
    
    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid:
            form.save(request.POST)
            return HttpResponse(400)
    