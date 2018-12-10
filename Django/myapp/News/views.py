from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import News
from .forms import registroform

def home(resquest):
	context = {
		"text": "jvrbaptista@live.com",
		"nomes": ["jvrbaptista@live.com", "@live.com", "ola", "Oii"]

	}
	return render(resquest, "home.html", context)

def contatos(resquest):
	context = {
		"text": "Variavel@live.com"
	}
	return render(resquest, "contato.html", context)

def Novidades_detalhes(resquest):
	obj = News.objects.get(id=1)
	context = {
		"object": obj

	}
	return render(resquest, "Novidades_detalhes.html", context)

def Novidades_anual(resquest, year):
	list = News.objects.filter(pub_date__year=year)
	context = {
		'year':year,
		'arquivo_list':list
	}
	return render(resquest, "Novidades_anual.html", context)

def registro(resquest):
	context = {
		"form": registroform

	}
	return render(resquest, "registro.html", context)

