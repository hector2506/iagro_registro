from django.contrib import admin

from registros.models import AbateDiario, Pedido, Romaneio


class AbateDiarioAdmin(admin.ModelAdmin):
    list_display = ("dia",)
    list_filter = ["dia"]
    fieldsets = [
        (None, {"fields": ["dia"]}),
        ("Cortes de Suínos", {"fields": ["cortes_suinos"]}),
        ("Cortes de Carneiros", {"fields": ["cortes_carneiros"]}),
    ]


admin.site.register(AbateDiario, AbateDiarioAdmin)
admin.site.register(Romaneio)
admin.site.register(Pedido)
