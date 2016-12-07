from django.views.generic import ListView, DetailView
from alumni.models import User


class UserSearchMixin(object):

    def get_queryset(self):
        # 부모의 get_queryset으로 부터 queryset을 가져옵니다.
        queryset = super(UserSearchMixin, self).get_queryset()

        # q라는 파라미터를 가져옵니다.
        q = self.request.GET.get("q")
        if q:
            # q가 이름에 포함되거나 핸드폰번호를 공개한 사람의 핸드폰 번호에 포함되면 결과를 냅니다.
            q1 = queryset.filter(name__icontains=q)
            q2 = queryset.filter(login_id__icontains=q)
            q2 = q2.exclude(open_login_id=False)
            queryset = q1 | q2
        return queryset


class UserLV(UserSearchMixin, ListView):
    model = User
    ordering = ["-period", ]


class ExecutiveLV(UserLV):
    queryset = User.objects.exclude(position='일반회원')


class UserDV(DetailView):
    model = User
    context_object_name = 'alumni'
