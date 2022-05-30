from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    # 커스텀 매니저 : 쿼리문을 변수처럼 저장해서 사용하기
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')


    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    # on_delete : 참조 무결성
    # on_delete = models.CASCADE -> ForeignKeyField를 포함하는 모델 인스턴스를 삭제
    # on_delete = models.PROTECT -> 해당 요소가 같이 삭제되지 않도록 ProtectedError를 발생시킨다
    # on_delete = models.SET_NULL -> ForeignKeyField 값을 NULL로 바꾼다. null=True일 때만 사용할 수 있다.
    # on_delete = models.SET_DEFAULT -> ForeignKeyField 값을 default 값으로 변경한다. default 값이 있을 때만 사용할 수 있다.
    # on_delete = models.SET -> ForeignKeyField 값을 SET에 설정된 함수 등에 의해 설정한다.
    # on_delete = models.DO_NOTHING -> 아무런 행동을 취하지 않는다. 참조 무결성을 해칠 위험이 있어서 잘 사용되지는 않는다.

    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published') # slug화 시킴 : 이쁜 URL로 만들어 줌
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=options, default='published')
    # options : 왼쪽 값이 들어가면 자동으로 오른쪽 값으로 치환

    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title