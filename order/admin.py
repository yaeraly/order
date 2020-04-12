from django.contrib import admin
from .models import Week, Menu, Food, Starter, MainCourse, Dessert

class MenuInline(admin.StackedInline):
    model = Menu
    extra = 7

class FoodInline(admin.StackedInline):
    model = Food
    extra = 1

class StarterInline(admin.StackedInline):
    model = Starter
    extra = 1

class MainCourseInline(admin.StackedInline):
    model = MainCourse
    extra = 1

class DessertInline(admin.StackedInline):
    model = Dessert
    extra = 1

class WeekAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Week', {'fields': ['week_number']}),
    ]
    inlines = [MenuInline]

class MenuAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Menu', {'fields': ['menu_number']}),
    ]
    inlines = [FoodInline]

class FoodAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Food', {'fields': ['food_name']}),
    ]
    inlines = [StarterInline, MainCourseInline, DessertInline]

admin.site.register(Week, WeekAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Menu, MenuAdmin)
