from django.db import models

from lms_app.professor import *
from lms_app.disciplina import *

class DisciplinaOfertada(models.Model):

    def save(self):
        
        if not(self.curso in ['ADS', 'SI', 'BD']):
            raise Exception("Curso invalido")
        
        if (len(DisciplinaOfertada.objects.filter(curso=self.curso, turma=self.turma, ano=self.ano, semestre=self.semestre, disciplina=self.disciplina)) > 0):
            raise Exception("Disciplina já ofertada")
        
        if (len(Professor.objects.filter(id=self.professor)) != 1):
            raise Exception("Id do professor invalido")
        
        if (len(Disciplina.objects.filter(id=self.disciplina)) != 1):
            raise Exception("Id da disciplina invalido")

        super(DisciplinaOfertada, self).save()

    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField() #um inteiro, representa um ano
    semestre = models.IntegerField() #um inteiro, 1 para primeiro sem e 2 para segundo
    professor = models.IntegerField() #id de um professor valido
    disciplina = models.IntegerField() #id de uma disciplina valida
