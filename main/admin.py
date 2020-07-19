from django.contrib import admin
from  .models import Msafiri, MsafiriCategory, MsafiriDetails

# Register your models here.
class MsafiriAdmin(admin.ModelAdmin):
	fieldsets = [
		 ("Title/date", {"Fields": ["msafiri_title", "msafiri_time"]}),
		 ("URL", {"fields": ["msafiri_slug"]}),
		 ("Details", {"fields": ["msafiri_details"]}),
		 ("Description", {"fields":["msafiri_description"]})

		 ]





admin.site.register(MsafiriCategory)

admin.site.register(MsafiriDetails)

admin.site.register(Msafiri)