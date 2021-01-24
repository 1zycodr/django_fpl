from modeltranslation.translator import register, TranslationOptions
from .models import Purchase, Category, Region, Asset, News, Leader, Document, Page, Directors, Government

@register(Purchase)
class PurchaseTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Asset)
class AssetTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'location', 'bargaining_link', 'as_type')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Leader)
class LeaderTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'description')

@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(Directors)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'description')

@register(Government)
class GovernmentTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'description')