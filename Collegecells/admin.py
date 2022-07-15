from django.contrib import admin
from Collegecells.models import cellEventplan_model,MOM_model,ClubEvent_model,member_model
# Register your models here.
admin.site.register(cellEventplan_model)
admin.site.register(MOM_model)
admin.site.register(ClubEvent_model)
admin.site.register(member_model)

