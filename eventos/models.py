from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    logradouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf = models.CharField(max_length=2, null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField(max_length=10)

    def __str__(self):
        '{}, {}, {}'.format(self.logradouro, self.cidade, self.uf)

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoas', null=True, blank=False)
    usuario = models.OneToOneField(User)
    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=128)
    mae = models.CharField(max_length=128)
    pai = models.CharField(max_length=128)

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField(max_length=400)
    sigra = models.CharField(max_length=128)
    numero = models.CharField(max_length=128)
    ano = models.CharField(max_length=128)
    realizador = models.ForeignKey(PessoaFisica, null = True, blank=False)
    endereco = models.ForeignKey(Endereco, null=True, blank=False)
    data_de_inicio = models.DateField(blank=True, null=True)
    data_de_fim = models.DateField(blank=True, null=True)

class Inscricao(models.Model):
    evento = models.ForeignKey(Evento)
    Pessoa = models.ForeignKey(PessoaFisica)
    data = models.DateTimeField()
