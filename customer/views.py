from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import User, Cart
from Chinese.models import Category, Food
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

# Create your views here.
class CustomerListView(ListView):
    model = Category
    template_name = 'customer/customer_index.html'
    # context_object_name = 'category'
    # def get_queryset(self) -> QuerySet[Any]:
    #     category = Category.objects.all()
    #     food = Food.objects.all()
    #     context = {
    #         'category': category,
    #         'food':food
    #     }
    #     return context
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        category = Category.objects.all()
        food = Food.objects.all()
        context = {
            'category': category,
            'food':food
        }
        return context
    

# def index(request):
#     category = Category.objects.all()
#     food = Food.objects.all()
#     context = {
#         'category':category,
#         'food':food
#     }
#     return render(request, 'home.html', context)
    

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     category = Category.objects.all()
    #     kwargs['category'] = category
    #     return super().get_context_data(**kwargs)
    

class CustomerDetailView(DetailView):
    template_name = 'customer/customer_detail.html'

    def get_queryset(self) -> QuerySet[Any]:
        # object 보내줘야 함
        pk = self.kwargs.get('pk')
        food = Food.objects.filter(pk=pk)
        return food

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     food = Food.objects.get(pk=self.kwargs['pk'])
    #     kwargs['food'] = food
    #     return super().get_context_data(**kwargs)


def add_cart(request):
    # Cart food_id에 대응되는 데이터의 수량을 add 하다(하나 올려라)
    food_id= request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    # 이전에 해당 음시에 대한 장바구니 정보가 있으면 get(food=food)
    # 없으면 새로 생성해서 적용
    try:
        cart = Cart.objects.get(food=food)
    except:
        cart = Cart.objects.create(food=food)
    finally:
        pass
    cart.amount+=1
    cart.save()
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html',context )


def remove_cart(request):
    food_id= request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    # cart, created = Cart.objects.get_or_create(food=food)    
    cart, _ = Cart.objects.get_or_create(food=food)    
    cart.amount-=1
    cart.save()
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html',context )


# cart page를 따로 만들기.
def modify_cart(request):
    # 어떤 음식(food_id)에 amount를 amountChange만큼 변경하고 <- 개발하기
    food_id= request.POST['foodId']
    food = Food.objects.get(pk=food_id)
    cart, _ = Cart.objects.get_or_create(food=food)
    cart.amount+=int(request.POST['amountChange'])
    if cart.amount>0:
        cart.save()
    # 변경된 최종 결과를 반환(JSON)
    context = {
        'newQuantity':cart.amount,
        'message':'수량이 성공적으로 업데이트 되었습니다.',
        'success':True
    }
    return JsonResponse(context)


class MRCreateView(CreateView):
    model= User
    template_name = 'customer/customer_pages.html'
    fields = ['user_name', 'user_phone']

    # def get_queryset(self) -> QuerySet[Any]:
    #     user = User.objects.all()
    #     return user

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        user = User.objects.all()
        context ={
            'user':user,
        }
        return context


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'



# def index(request):
#     form = None
#     # context = {'name': 'Alice'}  # 템플릿에 전달할 context 데이터
#     if request.method == 'POST':
#         category = Category.objects.get(name=request.POST.get('category'))
        
#         name = request.POST.get('username')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         food_takeout = request.POST['takeout']

#         form = FoodForm(request.POST, request.FILES)
#         if form.is_valid():
#             if 'file' in request.FILES:
#                 form.save()
                  
#             else:
#                 pass

#         # 이미지 저장 및 url 설정 내용
#         fs=FileSystemStorage()
#         uploaded_file = request.FILES['picture']
#         name = fs.save(uploaded_file.name, uploaded_file)
#         url = fs.url(name)

#         new_name = Food(category=category, name=name, description = description, price=price, image_url = url)
#         new_name.save()
#     elif request.method == 'GET':
#         pass
#     else:
#         form = FoodForm()
#     return render(request, 'Chinese/index.html', {'form' : form})
    

# def index_detail(request, pk):
#     object = Food.objects.get(pk=pk)
#     context = {
#         'object':object
#     }
#     return render(request, 'Chinese/index_detail.html', context)