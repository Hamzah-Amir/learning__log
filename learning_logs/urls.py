from django.urls import path
from . import views

app_name = "learning_logs"

urlpatterns = [
    #Home page
    path("", views.index, name="index"),
    # page to show all topics
    path("topics/", views.topics, name="topics"),
    path("topic/<int:topic_id>/", views.topic, name="topic"),
    # Path for adding new topics
    path("new_topic/", views.new_topic, name="new_topic"),
    # path for new entry
    path("new_entry/<int:topic_id>/", views.new_entry , name="new_entry"),
    # path for editing entries
    path("edit_entry/<int:entry_id>", views.edit_entry, name="edit_entry"),
]