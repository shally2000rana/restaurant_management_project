from django.db import models
class Feedback(models.Model):
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} -{self.created_at.strftime('%Y-%m-%d %H:%M)}"

from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['comment']
        widgets={
            'comment':forms.Textarea(attrs={
                'placeholder': 'write your feedback here...',
                'rows':4,
                'cols':40
            }),
        }

from django.shortcuts import render,
from .forms import FeedbackForm

def feedback_view(request):
    if request.method =="POST":
        form =FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form=FeedbackForm()
    return render(request, "feedback.html", {"form": form})        


 
