# -*- coding: utf-8 -*-

from django.db import models

class Meds(models.Model):
	CODIGO = models.IntegerField(
		blank=False,
		primary_key=True
	)
	DESCRICAO = models.CharField(
		max_length=255,
		blank=False
	)
	
	def __unicode__(self):
		return self.DESCRICAO

class Farma(models.Model):
	nome = models.CharField(
		max_length=300,
		blank=False
	)
	cidade = models.CharField(
		max_length=300,
		blank=False
	)
	bairro = models.CharField(
		max_length=300,
		blank=False
	)
	sec_id = models.IntegerField(
		blank=False
	)
	
	def __unicode__(self):
		return self.nome

class EstoqueFarma(models.Model):
	farma = models.ForeignKey(
		Farma
	)
	med = models.ForeignKey(
		Meds
	)
	qtde = models.IntegerField(
		blank=False
	)
	
	def __unicode__(self):
		return sellf.farma.nome + " : " + self.med.nome


