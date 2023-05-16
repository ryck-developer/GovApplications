from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.contrib.auth.views import LoginView
from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import View
from app.models import Product
from user_agents import parse
from app.models import User
from django.http import HttpResponse
from app.models import AllCookies
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import HttpResponse
from app.serializers import CookieSerializer
from rest_framework import status
from rest_framework.renderers import JSONRenderer



class AuthenticationForm(BaseAuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"autofocus": "true", 'type': 'email'}))

class LoginView(LoginView):
    template_name = 'app/login.html'
    authentication_form = AuthenticationForm
    def post(self, request, *args, **kwargs):
        # Captura o agente do usuário e o tipo de dispositivo
        user_agent = parse(request.META['HTTP_USER_AGENT'])
        browser = user_agent.browser.family
        device = user_agent.device.family
        ip_address = request.META['REMOTE_ADDR']

        # Dados recebidos via requisição POST
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Chama o método padrão de autenticação do Django
        response = super().post(request, *args, **kwargs)

        # Verifica se o login foi bem-sucedido
        if response.status_code == 302:
            # Obtém o usuário autenticado
            user = self.request.user


        return response



class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        # Verifica se o usuário existe no banco de dados
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=404)

        # Verifica se a senha está correta
        if not authenticate(username=user.email, password=password):
            return Response({'error': 'Senha incorreta'}, status=400)

        # Usuário autenticado com sucesso
        return Response({'message': 'Login bem-sucedido'})


        return response

class ReturnCookie(View):
    def get(self, request):
        # Obtém o token CSRF do cookie
        csrf_token = request.COOKIES.get('csrftoken')

        # Retorna o token CSRF como resposta
        if csrf_token:
            return HttpResponse(csrf_token)
        else:
            return HttpResponse("Cookie CSRF não encontrado.", status=400)
        


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))



@method_decorator(login_required, name='dispatch')
class IndexView(View):
    template_name = 'app/index.html'
    
    def get(self, request):
        products = Product.objects.filter(user=request.user)
        product_names = [
            {
                'nome': product.name,
                'url': product.link,
                'photo': product.img,
            } for product in products
        ]
        context = {'product_names': product_names}
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class AdspyView(TemplateView):
    template_name = 'app/adspy.html'
    def get(self, request, *args, **kwargs):
        if not Product.objects.filter(user=request.user, expires__gte=timezone.localtime().date(), name=Product.ProductName.ADSPY).first():
            return redirect(reverse_lazy('index'))
        return super().get(request, *args, **kwargs)


class AdvaultView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'app/advault.html'
        # Defina os cookies
        cookies = [
            {
                "domain": ".tubesift.com",
                "expirationDate": 1683535456.059413,
                "hostOnly": True,
                "httpOnly": False,
                "name": "PHPSESSID",
                "path": "/",
                "sameSite": None,
                "secure": False,
                "session": False,
                "storeId": None,
                "value": "q62ffmksv5p76eipbiovbfkhfl"
            }
        ]

        # Redirecione para a página desejada
        context = {}
        response = render(request, template_name, context)

        # Adicione os cookies ao cabeçalho da resposta
        for cookie in cookies:
            response.set_cookie(
                key=cookie['name'],
                value=cookie['value'],
                expires=cookie['expirationDate'],
                domain=cookie['domain'],
                path=cookie['path'],
                secure=cookie['secure'],
                httponly=cookie['httpOnly']
            )

        return response

       


class BigspyView(TemplateView):
    template_name = 'app/bigspy.html'
    def get(self, request, *args, **kwargs):
        # if not Product.objects.filter(user=request.user, expires__gte=timezone.localtime().date(), name=Product.ProductName.ADSPY).first():
        #     return redirect(reverse_lazy('index'))
        return super().get(request, *args, **kwargs)
    

class PipiadsView(TemplateView):
    def get(self, request, *args, **kwargs):
        if not Product.objects.filter(user=request.user, expires__gte=timezone.localtime().date(), name=Product.ProductName.ADSPY).first():
            return redirect(reverse_lazy('index'))
        template_name = 'app/pipiads.html'
        return render(request,template_name)
    
    
@method_decorator(login_required, name='dispatch')    
class AdheartNodeView(TemplateView):
    template_name = 'app/adheart-node.html'
    def get(self, request, *args, **kwargs):
        if not Product.objects.filter(user=request.user, expires__gte=timezone.localtime().date(), name=Product.ProductName.ADHEART2).first():
            return redirect(reverse_lazy('index'))
        return super().get(request, *args, **kwargs)
    

@method_decorator(login_required, name='dispatch')
class TesteSystem(TemplateView):
    template_name = 'app/adheart-node.html'
    print("-----------------------------2")
    def dispatch(self, request, *args, **kwargs):
        print("-----------------------------------")
        if not self.has_systemteste_product(request.user):
            return redirect(reverse_lazy('index'))
        return super().dispatch(request, *args, **kwargs)

    def has_systemteste_product(self, user):
        return Product.objects.filter(user=user, expires__gte=timezone.localtime().date(), name=Product.ProductName.ADHEART2).exists()



class HandlerCookie(APIView):
    def get(self, request, format=None):
        try:
            last_cookie = AllCookies.objects.last()
            serializer = CookieSerializer(last_cookie)
            return Response(serializer.data)
        except Exception:
            return Response({'notification': "sem cookies registrados"})
        
    def post(self,request):
        serializer = CookieSerializer(data=request.data)
        print(request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)