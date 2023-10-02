from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_list = []
        for form in self.forms:
            main_list.append(form.cleaned_data.get('is_main'))
        if main_list.count(True) == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_list.count(True) > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 6


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image',]
    inlines = [ScopeInline]
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id']