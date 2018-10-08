from django.db import models

class Aluno(models.Model):

    def save(self):
        if (self.email == ''):
            self.email = 'email nao fornecido'
        
        if (self.login == ''):
            raise Exception("Esta faltando o login")
        if (len(Aluno.objects.filter(login=self.login)) > 0):
            raise Exception("Aluno já cadastrado")
        # if (len(Professor.objects.filter(login=self.login)) > 0):
        #     raise Exception("Login já cadastrado")
        
        super(Aluno, self).save()
    
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)