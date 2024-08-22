from django.contrib import admin
from .models import Product, Order

# Register your models here.


admin.site.site_header = "Ecommerce Site"
admin.site.site_title = "Ecommerce"
admin.site.index_title = "Manage Ecommerce"


class ProductAdmin(admin.ModelAdmin):

    def changeCategoryToDefault(self, queryset):
        queryset.update(category='default')

    changeCategoryToDefault.short_description = "Change category to default"

    list_display = ('title', 'price', 'category', 'description')
    search_fields = ('title', 'category')
    actions = ('changeCategoryToDefault',)
    list_editable = ('price',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
