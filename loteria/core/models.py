from django.db import models

class Jogo(models.Model):
    id_jogo = models.IntegerField(verbose_name='Numero Jogo', null=True, blank=True)
    data = models.DateField(verbose_name='Data', null=True, blank=True)
    ganhador = models.IntegerField(verbose_name='Quantidade de Ganhador', null=True, blank=True)

    class Meta:
        ordering = ['-data']
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
    
    def __str__(self):
        return f'{self.id}'

class NumeroSorteado(models.Model):
    id_jogo = models.ForeignKey(Jogo, verbose_name='Numero Jogo', on_delete=models.CASCADE, null=True, blank=True)
    n1 = models.IntegerField(verbose_name='1', null=True, blank=True)
    n2 = models.IntegerField(verbose_name='2', null=True, blank=True)
    n3 = models.IntegerField(verbose_name='3', null=True, blank=True)
    n4 = models.IntegerField(verbose_name='4', null=True, blank=True)
    n5 = models.IntegerField(verbose_name='5', null=True, blank=True)
    n6 = models.IntegerField(verbose_name='6', null=True, blank=True)
    n7 = models.IntegerField(verbose_name='7', null=True, blank=True)
    n8 = models.IntegerField(verbose_name='8', null=True, blank=True)
    n9 = models.IntegerField(verbose_name='9', null=True, blank=True)
    n10 = models.IntegerField(verbose_name='10', null=True, blank=True)
    n11 = models.IntegerField(verbose_name='11', null=True, blank=True)
    n12 = models.IntegerField(verbose_name='12', null=True, blank=True)
    n13 = models.IntegerField(verbose_name='13', null=True, blank=True)
    n14 = models.IntegerField(verbose_name='14', null=True, blank=True)
    n15 = models.IntegerField(verbose_name='15', null=True, blank=True)
    n16 = models.IntegerField(verbose_name='16', null=True, blank=True)
    n17 = models.IntegerField(verbose_name='17', null=True, blank=True)
    n18 = models.IntegerField(verbose_name='18', null=True, blank=True)
    n19 = models.IntegerField(verbose_name='19', null=True, blank=True)
    n20 = models.IntegerField(verbose_name='20', null=True, blank=True)

    class Meta:
        ordering = ['-id_jogo']
        verbose_name = 'Numero Sorteado'
        verbose_name_plural = 'Numeros Sorteados'
    
    def __str__(self):
        return f'Números sorteados jogo {self.id_jogo}'

class NumeroRepetido(models.Model):
    id_jogo = models.ForeignKey(Jogo, verbose_name='Numero Jogo', on_delete=models.CASCADE, null=True, blank=True)
    n1 = models.IntegerField(verbose_name='1', null=True, blank=True)
    n2 = models.IntegerField(verbose_name='2', null=True, blank=True)
    n3 = models.IntegerField(verbose_name='3', null=True, blank=True)
    n4 = models.IntegerField(verbose_name='4', null=True, blank=True)
    n5 = models.IntegerField(verbose_name='5', null=True, blank=True)
    n6 = models.IntegerField(verbose_name='6', null=True, blank=True)
    n7 = models.IntegerField(verbose_name='7', null=True, blank=True)
    n8 = models.IntegerField(verbose_name='8', null=True, blank=True)
    n9 = models.IntegerField(verbose_name='9', null=True, blank=True)
    n10 = models.IntegerField(verbose_name='10', null=True, blank=True)
    

    class Meta:
        ordering = ['-id_jogo']
        verbose_name = 'Numero Repetido'
        verbose_name_plural = 'Numeros Repetidos'
    
    def __str__(self):
        return f'Números repetidos jogo {self.id_jogo}'

