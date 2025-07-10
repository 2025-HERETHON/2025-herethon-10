from django.urls import path
from community.views import comment_delete_view, comment_edit_view, comment_view, items_home_view, write_view, detail_view, tips_home_view, post_likes_view, post_update_view, post_delete_view, items_search_view, tips_search_view

app_name="community"

urlpatterns = [
    path('items/', items_home_view, name="items"),
    path('tips/', tips_home_view, name="tips"),
    path('write/', write_view, name="write"),
    path('detail/<int:post_id>/', detail_view, name="detail"),
    path('detail/<int:post_id>/likes/', post_likes_view, name="post_likes"),
    path('post_update/<int:post_id>/', post_update_view, name="post_update"),
    path('post_delete/<int:post_id>/', post_delete_view, name="post_delete"),
    path('detail/<int:post_id>/comment/', comment_view, name="comment"),
    path('comment/<int:comment_id>/delete/', comment_delete_view, name='comment_delete'),
    path('comment/<int:comment_id>/edit/', comment_edit_view, name='comment_edit'),
    
    path('items_search/', items_search_view, name="items_search"),
    path('tips_search/', tips_search_view, name="tips_search"),
]
