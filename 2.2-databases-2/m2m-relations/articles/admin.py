from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, RelationShip


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) < 2:
            raise ValidationError('Нужно выбрать ещё хотя бы одну дополнительную рубрику')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = RelationShip
    extra = 1
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class ThemeAdmin(admin.ModelAdmin):
    pass




