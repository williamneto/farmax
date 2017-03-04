# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.http import JsonResponse

from models import Meds

class IndexView(TemplateView):
	template_name = "index.html"
	get_services = ('search_autocomplete', )

	def get(self, *args, **kwargs):
		ctx = self.get_context_data()
		cmd = self.request.GET.get('cmd')

		if cmd and cmd in self.get_services:
			return getattr(self, '_%s' % cmd)()

		return super(IndexView, self).get(*args, **kwargs)
	
	def _search_autocomplete(self):
		text = self.request.GET['text']
		
		query = Meds.objects.all().filter(DESCRICAO__icontains=text)
		
		json = []
		for q in query:
			json.append(q.DESCRICAO)
		
		return JsonResponse(json, safe=False)
