#view
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SignupForm


def signup_view(request):
   # 회원 가입 view
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():         # 사용자가 입력정보를 제대로 입력했는지 유효성 판별
            form.save()             # 사용자 입력정보 저장
            return redirect('/sign-in')     # 로그인페이지로 리다이렉트
    else:
        # 이 경우는 사용자 입력이 잘못되었거나 등 이유로 새로운 페이지를 새로 랜더링 하기 위해서 필요한 코드
        form = SignupForm()    # 우선 새로운 페이지를 랜더링하기 위해서는 새로운 form 인스턴스를 생성해주어야 한다.
    return render(request, 'accounts/signup.html', {'form': form})   # 그리고 새로운 페이지를 랜더링 하면서 form 인스턴스를 같이 실어보낸다.


def login_view(request):
    # 로그인 view
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # 장고의 내장된 기본 로그인 폼
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # form.cleaned_data는 아래와 같이 데이터의 정제후 딕셔너리 형태로 가져오게 된다.
                                        # 데이터를 문자열 형태로 변환합니다.
                                        # 데이터를 불필요한 공백 문자를 제거합니다.
                                        # 필드별로 데이터를 유효한 형식으로 변환합니다.
                                        # 데이터를 유효성 검사를 수행합니다.
            user = authenticate(username=username, password=password)  # 이름과 비번을 확인하여 유효한 사용자인지 확인후 인스턴스를 반환한다
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})
def logout_view(request):
    # 로그아웃 view
    logout(request)
    return redirect('/sign-in')
    # response.delete_cookie('sessionid')
    pass