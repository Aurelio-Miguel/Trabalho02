from django.shortcuts import render
from django.http import HttpResponse

from agenda.models import Agenda

def agenda(request):
    lista_agenda = Agenda.objects.all()
    retorno = ""
    for agenda in lista_agenda:
        retorno += '<li>'.format(agenda.nome_agenda)+'</li>'
    return HttpResponse(retorno)

'''def agenda(request,id):
    lista_agenda = AgendaUsuario.objects.all()
    retorno = ""
    for agenda in lista_agenda:
        if id == agenda.usuario:
            retorno += "<li>"+agenda.nome+"</li>"
    return HttpResponse(retorno)'''
