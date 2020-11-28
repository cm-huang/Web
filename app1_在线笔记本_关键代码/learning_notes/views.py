from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Note
from .forms import TopicForm, NoteForm


def index(request):
    """学习笔记的主页。"""
    return render(request, 'learning_notes/index.html')


@login_required
def topics(request):
    """显示所有的主题。"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_notes/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题及其所有的条目。"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户。
    if topic.owner != request.user:
        raise Http404
    notes = topic.note_set.order_by('-date_added')
    context = {'topic': topic, 'notes': notes}
    return render(request, 'learning_notes/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题。"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
        form = TopicForm()
    else:
        # POST提交的数据：对数据进行处理。
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_notes:topics')

    # 显示空表单或指出表单数据无效。
    context = {'form': form}
    return render(request, 'learning_notes/new_topic.html', context)


@login_required
def new_note(request, topic_id):
    """在特定主题中添加新条目。"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据：创建一个空表单。
        form = NoteForm()
    else:
        # POST提交的数据：对数据进行处理。
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.topic = topic
            new_note.save()
            return redirect('learning_notes:topic', topic_id=topic_id)

    # 显示空表单或指出表单数据无效。
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_notes/new_note.html', context)


@login_required
def edit_note(request, note_id):
    """编辑既有条目。"""
    note = Note.objects.get(id=note_id)
    topic = note.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求：使用当前条目填充表单。
        form = NoteForm(instance=note)
    else:
        # POST提交的数据：对数据进行处理。
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_notes:topic', topic_id=topic.id)

    context = {'note': note, 'topic': topic, 'form': form}
    return render(request, 'learning_notes/edit_note.html', context)


@login_required
def delete_note(request, note_id):
    """删除既有条目。"""
    note = Note.objects.get(id=note_id)
    topic = note.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求：使用当前条目填充表单。
        form = NoteForm(instance=note)
    else:
        # POST提交的数据：对数据进行处理。
        note.delete()
        return redirect('learning_notes:topic', topic_id=topic.id)

    context = {'note': note, 'topic': topic, 'form': form}
    return render(request, 'learning_notes/delete_note.html', context)


@login_required
def delete_topic(request, topic_id):
    """删除既有主题。"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求：使用当前条目填充表单。
        form = TopicForm(instance=topic)
    else:
        # POST提交的数据：对数据进行处理。
        topic.delete()
        return redirect('learning_notes:topics')

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_notes/delete_topic.html', context)