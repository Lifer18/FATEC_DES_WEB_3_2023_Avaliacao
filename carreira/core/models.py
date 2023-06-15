from django.db import models
from django.utils import timezone

class CadastroModel(models.Model):
    selecionar_professor = (
        ('Orlando', 'ORLANDO SARAIVA JR'),
        ('Nilton', 'NILTON SACCO'),
        ('Joao', 'JOAO NETO'),
    )

    nome = models.CharField('nome',max_length=100)
    professor = models.CharField('professor',max_length=100, choices=selecionar_professor, default='Orlando')
    data = models.DateField(verbose_name='Data',default=timezone.now())

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Aluno'
