from django.contrib import admin
from IQAC.models import IQAC_COE_model,Aqar_model,MOM_model,iqacEvent_model,iqacmeeting_model,IQACmandatedoc_model
from IQAC.models import Actioniqac_model,Mouiqac_model,Infraiqac_model,addoncourse_model,auditRpt_model,CollegeauditRpt_model
from IQAC.models import  scholarshipdet_model,Financegrants_model,codeconduct_model,member_model
# Register your models here.
admin.site.register(IQAC_COE_model)
admin.site.register(Aqar_model)
admin.site.register(MOM_model)
admin.site.register(iqacEvent_model)
admin.site.register(iqacmeeting_model)
admin.site.register(IQACmandatedoc_model)
admin.site.register(Actioniqac_model)
admin.site.register(Mouiqac_model)
admin.site.register(Infraiqac_model)
admin.site.register(addoncourse_model)
admin.site.register(auditRpt_model)
admin.site.register(CollegeauditRpt_model)
admin.site.register(scholarshipdet_model)
admin.site.register(Financegrants_model)
admin.site.register(codeconduct_model)
admin.site.register(member_model)