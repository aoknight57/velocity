# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.title'
        db.add_column(u'tracker_post', 'title',
                      self.gf('django.db.models.fields.CharField')(default='title', max_length=500),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.title'
        db.delete_column(u'tracker_post', 'title')


    models = {
        u'tracker.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '500'})
        }
    }

    complete_apps = ['tracker']