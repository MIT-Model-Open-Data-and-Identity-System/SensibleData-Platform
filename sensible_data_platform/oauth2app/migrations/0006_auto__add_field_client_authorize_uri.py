# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Client.authorize_uri'
        db.add_column(u'oauth2app_client', 'authorize_uri',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Client.authorize_uri'
        db.delete_column(u'oauth2app_client', 'authorize_uri')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'oauth2app.accessrange': {
            'Meta': {'object_name': 'AccessRange'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        u'oauth2app.accesstoken': {
            'Meta': {'object_name': 'AccessToken'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2app.Client']"}),
            'expire': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1374003754'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1374000154'}),
            'mac_key': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'refresh_token': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "'10f1f4a709'", 'max_length': '10', 'blank': 'True', 'unique': 'True', 'db_index': 'True'}),
            'refreshable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'scope': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['oauth2app.AccessRange']", 'symmetrical': 'False'}),
            'token': ('django.db.models.fields.CharField', [], {'default': "'12c61c279e'", 'unique': 'True', 'max_length': '10', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'oauth2app.client': {
            'Meta': {'object_name': 'Client'},
            'api_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'authorize_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'client_owner_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'6f7a2873d5d177653a7752dbcb21f0'", 'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'redirect_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'registered_scope': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['oauth2app.AccessRange']", 'symmetrical': 'False'}),
            'secret': ('django.db.models.fields.CharField', [], {'default': "'a320892ec2f398f0cb2529c8f77b05'", 'unique': 'True', 'max_length': '30'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2app.ClientType']", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'oauth2app.clienttype': {
            'Meta': {'object_name': 'ClientType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'id_client'", 'max_length': '100'})
        },
        u'oauth2app.code': {
            'Meta': {'object_name': 'Code'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2app.Client']"}),
            'expire': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1374000273'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1374000153'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'c7a7910efbb83476dea6370defffff'", 'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'redirect_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'scope': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['oauth2app.AccessRange']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'oauth2app.macnonce': {
            'Meta': {'object_name': 'MACNonce'},
            'access_token': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2app.AccessToken']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nonce': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'})
        }
    }

    complete_apps = ['oauth2app']