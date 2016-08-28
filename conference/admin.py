from django.contrib import admin
from .models import Conference,Images,Papers,Page
from django.db.models import Q
# Register your models here.
class ConferenceAdmin(admin.ModelAdmin):
	# fields = ('confname', 'description', 'startdate')
	def get_form(self, request, obj=None, **kwargs):
		if request.user.is_superuser:
		    self.exclude = ()
		elif request.user.groups.filter(name='confmang').exists():
		    self.exclude = ('manager',) 
		return super(ConferenceAdmin, self).get_form(request, obj=None, **kwargs)

	def get_queryset(self, request):
		if request.user.is_superuser:
		    return Conference.objects.all()
		q1 = Q(manager=request.user)
		# q2 = Q(editors.filter(username=request.user.username))
		# q2 = Q(request.user in editors)
		return Conference.objects.filter(q1)

admin.site.register(Conference,ConferenceAdmin)
admin.site.register(Images)
admin.site.register(Papers)
admin.site.register(Page)
