settings.py
#urls.pyのnameをかく
LOGIN_REDIRECT_URL =''
login後
{{% if user.is_authenticated%}}
{{user.username}}さん、ようこそ
{%else%}
<p>ログインしていません</p>
{%endif%}

logout
{{% if user.is_authenticated%}}
{{user.username}}さん、ようこそ
<a href="{% url 'logout%}">ログアウト</a>
{%else%}
<p>ログインしていません</p>
{%endif%}
#urls.pyのnameをかく
LOGOUT_REDIRECT_URL =''

会員機能
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
#username,password,password(確認)の３つのフィールドで作られるフォーム
    form_class = UserCreationForm

    success_url = reverse_lazy('login')

    template_name = 'signup.html'

models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    age = models.IntegerField(null=True)

カスタムしたUserもでるをdjangoに伝える
settings.py
AUTH_USER_MODEL = 'login.CustomUser'
