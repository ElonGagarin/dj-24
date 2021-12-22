from .models import Article
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import TagList, Relationship

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        k = 0 
        name = []
        for form in self.forms:
            data = form.cleaned_data
            if data != {}:
                if data['is_main'] == True:
                    k+=1
                name.append(data['tag'].name)

        if k == 0:
            raise ValidationError('Должен быть хотябы один главный тег')
        if k > 1:
            raise ValidationError('Главный тег может быть только один')
        if len(name) != len(set(name)):
            raise ValidationError('Теги не должны повторяться')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    extra=1

@admin.register(TagList)
class ObjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]