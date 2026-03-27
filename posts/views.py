from django.shortcuts import render,redirect
from .forms import Blogform
from .models import BlogPost



def home(request):
  blogs=BlogPost.objects.all().order_by('created_on')
  blogscount=blogs.count()
  context={
    'blogs':blogs,
    'blogscount':blogscount,
  }
  return render(request,'posts/home.html',context)



def blogposts(request):
  context={}
  return render(request,'posts/blogposts.html',context)


def create(request):
  form=Blogform()
  if request.method == 'POST':
    form =Blogform(request.POST)
    if form.is_valid():
      title=form.cleaned_data['title']
      content= form.cleaned_data['content']

      blog=BlogPost(
        title=title,
        content=content
      )

      blog.save()
      return redirect('blogposts')


  context={'form':form}
  return render(request,'posts/create.html',context)


