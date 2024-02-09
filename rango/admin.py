from django.contrib import admin
from rango.models import Category, Page


# Define a custom Admin class for the Page model
class PageAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed and their order
    list_display = ('title',  'category', 'url')

# Register the Page model with the custom Admin class
admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Category, CategoryAdmin)
