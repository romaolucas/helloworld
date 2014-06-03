from django.db import models

# Create your models here.
class Knight(models.Model):
   SWORD_TYPE = (('zgts', 'Zangetsu'),
         ('exclb', 'Excalibur'),
         ('ms', 'Master Sword'),
         ('grsk', 'Power Sword'),
         ('dflt', 'Ordinary Sword'),
         )
   name = models.CharField(max_length = 150)
   sword = models.CharField(max_length = 255, choices = SWORD_TYPE, default = 'dflt')
   def __unicode__(self):
      return self.name

class Mage(models.Model):
   TYPE = (('sorc', 'Sorcerer'),
         ('druid', 'Druid'),
         ('summ', 'Summoner'),
         ('nec', 'Necromancer'),
         )
   name = models.CharField(max_length = 150)
   sword = models.CharField(max_length = 255, choices = TYPE, default = 'sorc')
   def __unicode__(self):
      return self.name

class Archer(models.Model):
   name = models.CharField(max_length = 150)
   badassery = models.DecimalField(max_digits = 10, decimal_places = 7,
         default = 6)
   def __unicode__(self):
      return self.name

class Barbarian(models.Model):
   WEAPON = (('ax', 'Axe'),
         ('swd', 'Sword'),
         ('mc', 'Mace'),
         ('sp', 'Spear'),
         )
   name = models.CharField(max_length = 150)
   badassery = models.DecimalField(max_digits = 10, decimal_places = 7, 
         default = 7)
   weapon = models.CharField(max_length = 255, choices = WEAPON, default = 'ax')
   def __unicode__(self):
      return self.name
