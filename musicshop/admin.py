from django.contrib import admin
from musicshop.models import *

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'agent_FIO', 'agent_telephone')
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    @admin.display(description="ФИО представител")
    def agent_FIO(self, obj):
        if obj.patronymic_name:
            return f"{obj.agent_firstname} {obj.agent_name[0]}. {obj.patronymic_name[0]}."
        return f"{obj.agent_firstname} {obj.agent_name[0]}."


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier_name')
    list_display_links = ('id',)
    ordering = ('id',)

    @admin.display(description='Поставщик')
    def supplier_name(self, obj):
        return obj.supplier.name

@admin.register(Pos_supply)
class Pos_supplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'supply', 'count')
    list_display_links = ('id',)
    list_editable = ('count',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_FIO', 'delivery_address', 'delivery_type', 'datetime_create')
    list_display_links = ('customer_FIO',)
    search_fields = ('delivery_address',)

    @admin.display(description="ФИО покупателя")
    def customer_FIO(self, obj):
        if obj.customer_patronymic:
            return f"{obj.customer_firstname} {obj.customer_name[0]}. {obj.customer_patronymic[0]}."
        return f"{obj.customer_firstname} {obj.customer_name[0]}."

@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'discount', 'count')
    list_editable = ('order', 'product', 'discount', 'count')
    list_display_links = None




@admin.register(Parametr)
class ParametrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Pos_parametr)
class Pos_parametrAdmin(admin.ModelAdmin):
    list_display = ('parametr', 'product', 'value')
    list_editable = ('parametr', 'product', 'value')
    list_display_links = None


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'brand', 'is_exist')
    search_fields = ('name',)
    list_filter = ('category', 'brand',)
    list_display_links = ('name',)
    ordering = ('-id',)

    
    
    
    
    
    
