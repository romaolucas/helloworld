# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mage'
        db.create_table(u'Race_mage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('sword', self.gf('django.db.models.fields.CharField')(default='sorc', max_length=255)),
        ))
        db.send_create_signal(u'Race', ['Mage'])


    def backwards(self, orm):
        # Deleting model 'Mage'
        db.delete_table(u'Race_mage')


    models = {
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