from django.contrib import admin

from main.models import State, StateCapital, City


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "zip_code")
    search_fields = ["name"]
    save_as = True


class StateCapitalAdmin(admin.ModelAdmin):
    list_display = ("name", "population")
    search_fields = ["name"]
    save_as = True


class StateCapitalInLine(admin.TabularInline):
    model = StateCapital
    readonly_fields = ('name', 'state', 'latitude', 'longitude', 'population')


class CityInLine(admin.TabularInline):
    model = City
    readonly_fields = ('name', 'county', 'state', 'latitude', 'longitude', 'zip_code')


class StateAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ("name", "abbreviation")
    search_fields = ["name"]
    inlines = [StateCapitalInLine, CityInLine]
    save_as = True

admin.site.register(City, CityAdmin)
admin.site.register(StateCapital, StateCapitalAdmin)
admin.site.register(State, StateAdmin)
