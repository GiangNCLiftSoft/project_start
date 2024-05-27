from django.shortcuts import render,get_object_or_404,redirect
from ..models import Tag

def add_tag(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Tag.objects.create(name=name)
        return redirect('index')
    return render(request, 'addtag.html')

def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    tag.delete()
    return redirect('index')

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})