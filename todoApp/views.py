from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from .models import todoModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import TodoForm
# Create your views here.

@login_required(login_url='login')
def logoutfunc(request):
    logout(request)
    return redirect('login')

class todoList(ListView):
    model = todoModel
    
class todoDetail(DetailView):
    model = todoModel
    
class todoView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        if User.objects.filter(username=request.POST.get('username')).exists():
            messages.error(request, "Username already exists.")
        user = User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'))
        user.save()
        messages.success(request, "Registered successfully. Please login.")
        return render(request,'login.html')
class todoLoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        print("POST")
        user = authenticate(request=request,username=request.POST.get('username'),password=request.POST.get('password'))
        if not user:
            messages.error(request,"invalid credentials")
            return redirect('login')
        
        messages.success(request,"Logged In")
        login(request,user)
        return redirect('home')


class todoHomeView(View):
    def get(self, request):
        todos = todoModel.objects.filter(user=request.user)  # Get all todo tasks
        
            
        form = TodoForm()  # Initialize the form for rendering
        return render(request, 'home.html', {'todos': todos, 'form': form})

    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('home')
        todos = todoModel.objects.filter(user=request.user)
        return render(request, 'home.html', {'todos': todos, 'form': form})
    
class todoEdit(UpdateView):
    model = todoModel
    fields = ['task']
    success_url = reverse_lazy('home')
    def get_object(self):
        # Ensure the todo is retrieved correctly by primary key
        return get_object_or_404(todoModel, pk=self.kwargs['pk'])
    def get_queryset(self):
        return todoModel.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class todoDelete(DeleteView):
    model = todoModel
    success_url = reverse_lazy('home')
    
    def get_queryset(self):
        return todoModel.objects.filter(user=self.request.user)

    # Skipping confirmation by handling delete in GET request
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    
    
    
class todoCreate(CreateView):
    model = todoModel
    template_name = 'home.html'
    context_object_name = 'form'
    fields = ['task']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        # Automatically set the user to the currently authenticated user
        form.instance.user = self.request.user
        return super().form_valid(form)
    
