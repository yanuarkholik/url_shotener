from mc_tasklist import views
urlpatterns = [
    # ...
    path('add', views.add),
    path('remove', views.remove),
    path('', views.index),
]