from django.contrib import admin
from .models import Category, Document, Region, Asset, Page, Purchase, News, Leader, Results, FinOtchet, Audit, Government, Directors

admin.site.register(Asset)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Purchase)
admin.site.register(News)
admin.site.register(Results)
admin.site.register(FinOtchet)
admin.site.register(Document)
admin.site.register(Audit)
admin.site.register(Page)
admin.site.register(Directors)
admin.site.register(Government)