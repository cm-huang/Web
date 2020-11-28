"""定义learning_notes的URL模式。"""

from django.urls import path

from . import views

app_name = 'learning_notes'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path('new_note/<int:topic_id>/', views.new_note, name='new_note'),
    # 用于编辑条目的页面
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    # 用于删除条目的页面
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    # 用于删除主题的页面
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic')
]
