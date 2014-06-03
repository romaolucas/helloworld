# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Barbarian'
        db.create_table(u'Race_barbarian', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('badassery', self.gf('django.db.models.fields.DecimalField')(default=7, max_digits=10, decimal_places=7)),
            ('weapon', self.gf('django.db.models.fields.CharField')(default='ax', max_length=255)),
        ))
        db.send_create_signal(u'Race', ['Barbarian'])


    def backwards(self, orm):
        # Deleting model 'Barbarian'
        db.delete_table(u'Race_barbarian')


    models = {
        u'Race.archer': {
            'Meta': {'object_name': 'Archer'},
            'badassery': ('django.db.models.fields.DecimalField', [], {'default': '6', 'max_digits': '10', 'decimal_places': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'Race.barbarian': {
            'Meta': {'object_name': 'Barbarian'},
            'badassery': ('django.db.models.fields.DecimalField', [], {'default': '7', 'max_digits': '10', 'decimal_places': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'weapon': ('django.db.models.fields.CharField', [], {'default': "'ax'", 'max_length': '255'})
        },
        u'Race.knight': {
            'Meta': {'object_name': 'Knight'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sword': ('django.db.models.fields.CharField', [], {'default': "'dflt'", 'max_length': '255'})
        },
        u'Race.mage': {
            'Meta': {'object_name': 'Mage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sword': ('django.db.models.fields.CharField', [], {'default': "'sorc'", 'max_length': '255'})
        }
    }

    complete_apps = ['Race']