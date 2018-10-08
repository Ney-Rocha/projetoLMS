from django.db import models

class Professor(models.Model):
    def __str__(self):
        return self.nome + " - "+ self.email

    def save(self):
        print('estou salvando!')
        if(self.login == ''):
            raise Exception('login nao enviado')
            print("Sem login")
        
        if(self.email==''):
            self.email='email nao fornecido'

        if (len(Professor.objects.filter(login=self.login)) > 0):
            raise Exception("Esse login ja esta cadastrado")
        
        # if (len(Aluno.objects.filter(login=self.login)) > 0):
        #    raise Exception("Login já cadastrado")

        super(Professor,self).save()

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)