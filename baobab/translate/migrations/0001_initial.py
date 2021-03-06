# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lang'
        db.create_table('translate_lang', (
            ('id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=200)),
            ('iso', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=5)),
        ))
        db.send_create_signal('translate', ['Lang'])

        # Adding model 'EventData'
        db.create_table('translate_eventdata', (
            ('id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='eventdatas', to=orm['backoffice.Event'])),
            ('lang', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='eventdatas', to=orm['translate.Lang'])),
            ('title', self.gf('django.db.models.fields.CharField')
             (max_length=255)),
            ('summary', self.gf('django.db.models.fields.TextField')
             (default=None, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(
                default=None, related_name='eventdatas', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('translate', ['EventData'])

        # Adding unique constraint on 'EventData', fields ['event', 'lang']
        db.create_unique('translate_eventdata', ['event_id', 'lang_id'])

        # Adding model 'EventLogData'
        db.create_table('translate_eventlogdata', (
            ('id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('eventlog', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='eventlogdatas', to=orm['backoffice.EventLog'])),
            ('lang', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='eventlogdatas', to=orm['translate.Lang'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(
                default=None, related_name='eventlogdatas', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('translate', ['EventLogData'])

        # Adding unique constraint on 'EventLogData', fields ['eventlog',
        # 'lang']
        db.create_unique('translate_eventlogdata', ['eventlog_id', 'lang_id'])

    def backwards(self, orm):
        # Removing unique constraint on 'EventLogData', fields ['eventlog',
        # 'lang']
        db.delete_unique('translate_eventlogdata', ['eventlog_id', 'lang_id'])

        # Removing unique constraint on 'EventData', fields ['event', 'lang']
        db.delete_unique('translate_eventdata', ['event_id', 'lang_id'])

        # Deleting model 'Lang'
        db.delete_table('translate_lang')

        # Deleting model 'EventData'
        db.delete_table('translate_eventdata')

        # Deleting model 'EventLogData'
        db.delete_table('translate_eventlogdata')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'backoffice.event': {
            'Meta': {'ordering': "['id', 'pk']", 'object_name': 'Event'},
            'category': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'estimate_date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'msg_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events'", 'symmetrical': 'False', 'to': "orm['backoffice.Service']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'backoffice.eventlog': {
            'Meta': {'ordering': "['-date']", 'object_name': 'EventLog'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eventlogs'", 'to': "orm['backoffice.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'msg_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eventlogs'", 'to': "orm['auth.User']"})
        },
        'backoffice.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.PositiveSmallIntegerField', [], {'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'translate.eventdata': {
            'Meta': {'unique_together': "(('event', 'lang'),)", 'object_name': 'EventData'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eventdatas'", 'to': "orm['backoffice.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eventdatas'", 'to': "orm['translate.Lang']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'eventdatas'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'translate.eventlogdata': {
            'Meta': {'unique_together': "(('eventlog', 'lang'),)", 'object_name': 'EventLogData'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'eventlog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eventlogdatas'", 'to': "orm['backoffice.EventLog']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eventlogdatas'", 'to': "orm['translate.Lang']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'eventlogdatas'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'translate.lang': {
            'Meta': {'object_name': 'Lang'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['translate']
