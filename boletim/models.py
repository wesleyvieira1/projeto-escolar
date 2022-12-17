from django.db import models

class Boletim(models.Model):
    nota1b1 = models.IntegerField()
    nota2b1 = models.IntegerField()
    nota3b1 = models.IntegerField()
    bimestral1 = models.IntegerField()
    media1 = models.IntegerField()

    nota1b2 = models.IntegerField()
    nota2b2 = models.IntegerField()
    nota3b2 = models.IntegerField()
    bimestral2 = models.IntegerField()
    media2 = models.IntegerField()

    nota1b3 = models.IntegerField()
    nota2b3 = models.IntegerField()
    nota3b3 = models.IntegerField()
    bimestral3 = models.IntegerField()
    media3 = models.IntegerField()

    nota1b4 = models.IntegerField()
    nota2b4 = models.IntegerField()
    nota3b4 = models.IntegerField()
    bimestral4 = models.IntegerField()
    media4 = models.IntegerField()

    mediafinal = models.IntegerField()

    def __str__(self) -> str:
        return self.media1, self.media2, self.media3, self.media4
