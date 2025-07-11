from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render

from community.forms import PostForm
from community.models import Comment, Like, Post
from user.models import IndependencePlan
from django.db.models import Q
from django.shortcuts import render
from django.db.models import Q, Case, When, IntegerField, Value, Sum
from django.core.paginator import Paginator

# Create your views here.
def items_home_view(request):
    user=request.user
    independence = IndependencePlan.objects.get(user=user)
    base_qs =Post.objects.filter(board='shared_items', area_si=independence.area_si, area_sgg=independence.area_sgg).order_by('-created_at')
    
    # ✅ 페이징 처리
    page = request.GET.get('page', 1)
    paginator = Paginator(base_qs, 15)  # 한 페이지에 15개
    page_obj = paginator.get_page(page)
    
    
    return render(request, 'item_home.html', {'items_posts':page_obj, 'page_obj': page_obj, 'independence': independence})

def items_search_view(request):

    search_query = request.GET.get('searchbar', '').strip()
    page = request.GET.get('page', 1)
    
    independence = IndependencePlan.objects.get(user=request.user)
    
    base_qs = Post.objects.filter(
        board='shared_items',
        area_si=independence.area_si,
        area_sgg=independence.area_sgg
    )
    
    if search_query:
        import re
        keywords = re.split(r'[,\s]+', search_query)
        keywords = [kw for kw in keywords if kw]

        # 전체 검색어도 포함 (중복될 수 있으니 체크)
        if search_query and search_query not in keywords:
            keywords.append(search_query)
            
        # 각 키워드별 포함 여부를 Boolean으로 Annotate 후 합산
        qs = base_qs
        for i, kw in enumerate(keywords):
            kw_filter = Q(**{f'title__icontains': kw})
            qs = qs.annotate(**{
                f'kw_match_{i}': Case(
                    When(kw_filter, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField()
                )
            })
        
        # 모든 kw_match_* 필드를 더해서 match_count 생성
        kw_fields = [f'kw_match_{i}' for i in range(len(keywords))]
        from django.db.models import F
        total_expr = sum(F(f) for f in kw_fields)
        
        filtered_qs = qs.annotate(match_count=total_expr).filter(match_count__gt=0).order_by('-match_count', '-created_at')

    else:
        filtered_qs = base_qs.order_by('-created_at')
        
    paginator = Paginator(filtered_qs, 15)
    page_obj = paginator.get_page(page)
        
    context = {
        'items_posts': page_obj,
        'search_query': search_query,
        'page_obj': page_obj,
    }
    
    return render(request, 'test_items_search_results.html', context)

def tips_home_view(request):
    user=request.user
    independence = IndependencePlan.objects.get(user=user)
    base_qs=Post.objects.filter(board='resident_tips', area_si=independence.area_si, area_sgg=independence.area_sgg).order_by('-created_at')
    
    # ✅ 페이징 처리
    page = request.GET.get('page', 1)
    paginator = Paginator(base_qs, 15)  # 한 페이지에 15개
    page_obj = paginator.get_page(page)
    
    return render(request, 'tips_home.html', {'tips_posts':page_obj, 'page_obj': page_obj, 'independence':independence})

def tips_search_view(request):

    search_query = request.GET.get('searchbar', '').strip()
    page = request.GET.get('page', 1)
    
    independence = IndependencePlan.objects.get(user=request.user)
    
    base_qs = Post.objects.filter(
        board='resident_tips',
        area_si=independence.area_si,
        area_sgg=independence.area_sgg
    )
    
    if search_query:
        import re
        keywords = re.split(r'[,\s]+', search_query)
        keywords = [kw for kw in keywords if kw]

        # 전체 검색어도 포함 (중복될 수 있으니 체크)
        if search_query and search_query not in keywords:
            keywords.append(search_query)
            
        # 각 키워드별 포함 여부를 Boolean으로 Annotate 후 합산
        qs = base_qs
        for i, kw in enumerate(keywords):
            kw_filter = Q(**{f'title__icontains': kw})
            qs = qs.annotate(**{
                f'kw_match_{i}': Case(
                    When(kw_filter, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField()
                )
            })
        
        # 모든 kw_match_* 필드를 더해서 match_count 생성
        kw_fields = [f'kw_match_{i}' for i in range(len(keywords))]
        from django.db.models import F
        total_expr = sum(F(f) for f in kw_fields)
        
        filtered_qs = qs.annotate(match_count=total_expr).filter(match_count__gt=0).order_by('-match_count', '-created_at')

    else:
        filtered_qs = base_qs.order_by('-created_at')
        
    paginator = Paginator(filtered_qs, 15)
    page_obj = paginator.get_page(page)
        
    context = {
        'tips_posts': page_obj,
        'search_query': search_query,
        'page_obj': page_obj,
    }
    
    return render(request, 'test_tips_search_results.html', context)



def write_view(request):
    user=request.user
    independence = IndependencePlan.objects.get(user=user)
    
    if request.method == "POST":
        board = request.POST.get('board')
        post_type = request.POST.get("post_type")
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        print("board:", board)
        print("post_type:", post_type)
        print("title:", title)
        print("content:", content)
        print("image:", image)

        if not all([board, post_type, title, content]):
            return render(request, 'write.html', {
                'error': '모든 필드를 입력해주세요.'
            })

        Post.objects.create(
            user=request.user,
            board=board,
            post_type=post_type,
            title=title,
            content=content,
            image=image,
            area_si=independence.area_si,
            area_sgg=independence.area_sgg
        )

        return redirect("community:items")

    return render(request, 'write.html',{'independence':independence})

# def write_view(request):
#     user=request.user
#     independence = IndependencePlan.objects.get(user=user)
#     if request.method == 'POST':
#         post_form=PostForm(request.POST)
#         if post_form.is_valid():
#             post = post_form.save(commit=False)
#             post.user = request.user
#             post.area_si=independence.area_si
#             post.area_sgg=independence.area_sgg
#             post.image=request.FILES.get('image')
#             post.save()
#             # for img in request.FILES.getlist('image', None):
#             #     Image.objects.create(post=post, image=img)
#             return redirect('community:items')
#         return redirect('community:write')
#     else:
#         post_form = PostForm()
#         return render(request, 'write.html', {'post_form':post_form, 'independence':independence})
    
def detail_view(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    # images=Image.objects.filter(post=post)
    is_liked = False
    # comments=Comment.objects.filter(post=post)
    # post.views+=1
    if request.user.is_authenticated:
        is_liked = Like.objects.filter(post=post, user=request.user).exists()
        
    # print(">>> 좋아요 수:", post.like_set.count())  # 로그에 찍히는지 확인!    
    
    context={
        'post':post,
        # 'images':images,
        'is_liked': is_liked,
        # 'comments':comments,
    }
    return render(request, 'detail.html', context)

def post_likes_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user.is_authenticated:
        # 이미 좋아요 눌렀는지 확인
        existing_like = Like.objects.filter(user=request.user, post=post).first()

        if existing_like:
            existing_like.delete()  # 좋아요 취소
        else:
            Like.objects.create(user=request.user, post=post)  # 좋아요 생성

        return redirect('community:detail', post_id=post_id)

    return redirect('user:login')

def post_update_view(request, post_id):
    user = request.user
    independence = get_object_or_404(IndependencePlan, user=user)
    post = get_object_or_404(Post, id=post_id, user=user)  # 자신의 글만 수정 가능

    if request.method == 'POST':
        # 삭제 버튼 눌렀는지 확인
        if 'delete_image' in request.POST:
            post.image.delete(save=False)  # 파일 삭제
            post.image = None
            post.save()
            return redirect('community:post_update', post_id=post.id)

        u_board = request.POST.getlist('u_board')
        u_post_type = request.POST.get('u_post_type')
        u_title = request.POST.get('u_title')
        u_content = request.POST.get('u_content')
        new_image = request.FILES.get('image')

        if not all([u_board, u_post_type, u_title, u_content]):
            return render(request, 'update.html', {
                'independence': independence,
                'post': post,
                'error': '모든 항목을 입력해주세요.'
            })

        post.board = u_board[0]  # 단일 선택만 저장
        post.post_type = u_post_type
        post.title = u_title
        post.content = u_content

        if new_image:
            post.image = new_image

        post.save()

        return redirect('community:detail', post_id=post.id)

    return render(request, 'update.html', {
        'independence': independence,
        'post': post
    })
    
    
def post_delete_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('community:list')

def comment_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        comment_content = request.POST['comments']
        
        new_comment = Comment(post=post, content=comment_content, created_at=timezone.now(), user=request.user)
        
        new_comment.save() 
        
        return redirect('community:detail', post_id=post_id)
    
    return redirect('pcommunityost:detail', post_id=post_id)

def comment_delete_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user:
        post_id = comment.post.id
        comment.delete()
        return redirect('community:detail', post_id=post_id)
    return redirect('community:detail', post_id=comment.post.id)


def comment_edit_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        return redirect('community:detail', post_id=comment.post.id)

    if request.method == 'POST':
        new_content = request.POST.get('content')
        if new_content:
            comment.content = new_content
            comment.save()
        return redirect('community:detail', post_id=comment.post.id)

    return render(request, 'test_comment_edit.html', {'comment': comment})
