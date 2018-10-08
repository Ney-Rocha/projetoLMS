from django.db import models

class Matricula (models.Model):

    def save(self):
        if (len(Matricula.objects.filter(aluno=self.aluno)) >= 3):
            raise Exception("Aluno já possui 3 disciplinas cadastradas")

        if (len(Matricula.objects.filter(aluno=self.aluno, disciplinaOfertada=self.disciplinaOfertada)) > 0):
            print('ola')
            alu = Matricula.objects.filter(aluno=self.aluno)
            disOf = DisciplinaOfertada.objects.filter(id = self.disciplinaOfertada)
            dis = disOf[0].disciplina
            print('olaaa')
            for key in alu:
                print('ola')
                if (len(DisciplinaOfertada.objects.filter(id=key.disciplinaOfertada, disciplina=dis)) > 0):
                    raise Exception("Disciplina já cadastrada para esse aluno")

        super(Matricula, self).save()
    
    aluno = models.IntegerField()
    disciplinaOfertada = models.IntegerField()