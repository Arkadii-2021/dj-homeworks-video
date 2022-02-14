from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Heading, HeadingArticle


class HeadingArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_group = self.cleaned_data
        tags = []

        for is_tag in is_main_group:
            if is_tag.get('is_main'):
                tags.append(is_tag.get('is_main'))

        if len(tags) > 1 or len(tags) == 0:
            raise ValidationError('Требуется выбрать одну основную рубрику в данной статье')

        if len(self.forms) < 2:
            raise ValidationError('Необходимо выбрать одну дополнительную рубрику')
        return super().clean()


class HeadingArticleInline(admin.TabularInline):
    model = HeadingArticle
    extra = 1
    formset = HeadingArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [HeadingArticleInline]


@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
    pass




