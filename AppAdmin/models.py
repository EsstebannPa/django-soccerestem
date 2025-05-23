from django.db import models
from datetime import datetime
from PIL import Image



class Posiciones(models.Model):
    id_pos = models.BigAutoField(primary_key=True)
    nom_pos = models.CharField(max_length=40, verbose_name='Nombre Posición')
    des_pos = models.TextField(verbose_name='Descripción Posición')

    def __str__(self):
        return self.nom_pos
    
    class Meta:
        verbose_name = 'Posiciones'
        verbose_name_plural = 'Posición'
        db_table = 'posiciones'


class Equipos(models.Model):
    id_equipo = models.BigAutoField(primary_key=True)
    nom_equipo = models.CharField('Equipo', max_length=100)
    des_equipo = models.TextField(verbose_name='Descripción Equipo')
    ban_equipo = models.ImageField(verbose_name='Bandera', upload_to='media/', null=True, blank=True)
    esc_equipo = models.ImageField(verbose_name='Escudo', upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.nom_equipo

    class Meta:
        verbose_name = 'Equipos'
        verbose_name_plural = 'Equipo'
        db_table = 'equipos'

    
Rol_Tecnico = [
        ('Técnico', 'Técnico'),
        ('Asistente', 'Asistente'),
        ('Médico', 'Médico'),
        ('Preparador', 'Preparador'),
    ]


class Tecnicos(models.Model):
    id_tecnico = models.BigAutoField(primary_key=True)
    nom_tec = models.CharField('Nombre Técnico', max_length=100)
    apll_tec = models.CharField('Apellido Técnico', max_length=100)
    fecha_nac_tec = models.DateField()
    nacionalidad_tec = models.CharField('Nacionalidad Técnico', max_length=100)
    rol_tec = models.CharField(max_length=10, choices=Rol_Tecnico, null=True, help_text='Seleccione el rol')
    id_equipo = models.ForeignKey(Equipos, on_delete=models.PROTECT)


    def __str__(self):
        return self.nom_tec + self.apll_tec

    class Meta:
        verbose_name = 'Tecnicos'
        verbose_name_plural = 'Tecnico'
        db_table = 'tecnicos'


class Jugadores(models.Model):
    id_jugador = models.BigAutoField(primary_key=True)
    nom_jug = models.CharField('Nombre Jugador', max_length=100)
    apll_jug = models.CharField('Apellido Jugador', max_length=100)
    foto_jug = models.ImageField(upload_to='media/', null=True, blank=True)
    edad_jug = models.IntegerField()
    fecha_nac_jug = models.DateField()
    num_cams = models.IntegerField()
    titular = models.BooleanField(verbose_name='Titular Sí', default=True)
    id_equipo = models.ForeignKey(Equipos, verbose_name='Equipo Jugador', on_delete=models.PROTECT)
    id_posicion = models.ForeignKey(Posiciones, verbose_name='Posicion Jugador', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nom_jug + self.apll_jug


    class Meta:
        verbose_name = 'Jugadores'
        verbose_name_plural = 'Jugador'
        db_table = 'Jugadores'
