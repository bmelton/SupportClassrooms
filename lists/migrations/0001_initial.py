# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'lists_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.School'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('list_count', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'lists', ['Category'])

        # Adding model 'List'
        db.create_table(u'lists_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.School'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lists.Category'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'lists', ['List'])

        # Adding model 'Item'
        db.create_table(u'lists_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.School'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lists.Category'], null=True, blank=True)),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lists.List'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'lists', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'lists_category')

        # Deleting model 'List'
        db.delete_table(u'lists_list')

        # Deleting model 'Item'
        db.delete_table(u'lists_item')


    models = {
        u'lists.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.School']"})
        },
        u'lists.item': {
            'Meta': {'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lists.Category']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lists.List']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.School']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'lists.list': {
            'Meta': {'object_name': 'List'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lists.Category']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.School']"})
        },
        u'school.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'background': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'principal': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.State']", 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'school.state': {
            'Meta': {'object_name': 'State'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lists']