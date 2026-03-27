from django import forms
from .models import *

class Blogform(forms.ModelForm):
  title=forms.CharField(
    label='Blog post title',
    max_length=100,
    widget=forms.TextInput(attrs={
      'placeholder':'Enter the title of blog post...'
    })
  )

  content=forms.CharField(
    label='content',
    widget=forms.TextInput(attrs={
      'placeholder':'Write Your blog post...'
    })
  )

  class Meta:
    model=BlogPost
    fields=['title','content']
  

