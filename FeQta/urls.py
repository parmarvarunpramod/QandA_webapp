from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

# use app_name as namespace
app_name = 'FeQta'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name="home"),
    path('topics/', views.TopicListView.as_view(), name="topic_list"),
    path('topics/add-topic/', views.TopicCreateView.as_view(), name="topic_create"),
    path('topics/<slug>/', views.TopicDetailView.as_view(), name="topic_detail"),
    path('ask/', views.QuestionCreateView.as_view(), name="question_create"),
    path('question/<slug>/',views.QuestionDetailView.as_view(), name="question_detail"),
    path('answers/', views.AnswersView.as_view(), name="answers"),
    path('ranks/', views.RanksView.as_view(), name="ranks"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('get-started/', LoginView.as_view(), name="login"),
]

# path('topics/<slug1>/<slug2>/',views.QuestionDetailView.as_view(), name="question_detail"),