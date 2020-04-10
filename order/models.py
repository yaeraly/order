from django.db import models

class Week(models.Model):
    week_number = models.CharField(max_length=10)

    def __str__(self):
        return self.week_number

class Menu(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    menu_number = models.CharField(max_length=10)

    def __str__(self):
        return self.menu_number

class Food(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=10)

    def __str__(self):
        return self.food_name

class Starter(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    starter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.starter_name

class MainCourse(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    main_course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.main_course_name

class Dessert(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    dessert_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dessert_name
