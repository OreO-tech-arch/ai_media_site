from django.shortcuts import render, get_object_or_404  # ← get_object_or_404を追加
from .models import Post

# 一覧ページ（さっき作ったもの）
def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# ↓ 詳細ページ（新しく追加！）
def post_detail(request, pk):
    # pk(ID)の記事を探す。もしなかったら404エラー（見つかりません）を出す
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})