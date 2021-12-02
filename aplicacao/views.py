from django.core.mail import message
from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from  django.contrib import messages


from .models import Produto

def index(request):
  produtos = Produto.objects.all()
  context = {
    'produtos':  produtos
  }
  return render(request,'index.html', context)



def contato(request):
  #Pode conter dados não ser enviado e não ao ser renderizado pela página 
  form = ContatoForm(request.POST or None)

  if str(request.method) == 'POST':
    if form.is_valid():
      form.send_mail()
      messages.success(request,'Email enviado com sucesso!')
      form = ContatoForm()

    else:
      messages.error(request, 'Error ao enviar e-mail')
      
  context = {
    'form' : form
  }
  return render(request,'contato.html', context)


def produto(request):

  if str(request.method) == 'POST':
    form = ProdutoModelForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()

      messages.success(request, 'Produto salvo com sucesso.')
      form = ProdutoModelForm()
    else:
      messages.error(request, 'Error ao salvar o produto')
  
  else:
    form = ProdutoModelForm()
  context = {
      'form' : form
    }
  return render(request,'produto.html',context)



