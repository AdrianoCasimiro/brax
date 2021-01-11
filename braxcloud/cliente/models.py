from django.db import models


class Cliente(models.Model):
    STATE_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
        ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]
    cnpj = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=150)
    nome_fantasia = models.CharField(max_length=150)
    endereco = models.CharField(max_length=200)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=STATE_CHOICES)
    cep = models.CharField(max_length=10)
    serv_descarga_parcial = models.BooleanField(default=False)
    serv_temperatura = models.BooleanField(default=False)
    contato1_nome = models.CharField(max_length=150, blank=True, null=True)
    contato1_setor = models.CharField(max_length=150, blank=True, null=True)
    contato1_fone = models.CharField(max_length=150, blank=True, null=True)
    contato1_email = models.CharField(max_length=150, blank=True, null=True)
    contato2_nome = models.CharField(max_length=150, blank=True, null=True)
    contato2_setor = models.CharField(max_length=150, blank=True, null=True)
    contato2_fone = models.CharField(max_length=150, blank=True, null=True)
    contato2_email = models.CharField(max_length=150, blank=True, null=True)
    email_alerta = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.razao_social


class Planta(models.Model):
    nome = models.CharField(max_length=150)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name='clientes')

    class Meta:
        verbose_name = 'planta'
        verbose_name_plural = 'plantas'

    def __str__(self):
        return self.nome


class Setor(models.Model):
    nome = models.CharField(max_length=150)
    planta = models.ForeignKey('Planta', on_delete=models.CASCADE, verbose_name='plantas')

    class Meta:
        verbose_name = 'setor'
        verbose_name_plural = 'setores'

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    tag = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    setor = models.ForeignKey('Setor', on_delete=models.CASCADE, verbose_name='setores')
    temperatura_max = models.IntegerField(default=0, blank=True)

    class Meta:
        verbose_name='equipamento'
        verbose_name_plural='equipamentos'

    def __str__(self):
        return self.tag
