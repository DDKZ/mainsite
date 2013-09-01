# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'RequirementArea.campus'
        db.alter_column('coursesearch_requirementarea', 'campus', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'Meeting.campus'
        db.alter_column('coursesearch_meeting', 'campus', self.gf('django.db.models.fields.SmallIntegerField')())
    def backwards(self, orm):

        # Changing field 'RequirementArea.campus'
        db.alter_column('coursesearch_requirementarea', 'campus', self.gf('django.db.models.fields.PositiveSmallIntegerField')())

        # Changing field 'Meeting.campus'
        db.alter_column('coursesearch_meeting', 'campus', self.gf('django.db.models.fields.PositiveSmallIntegerField')())
    models = {
        'coursesearch.course': {
            'Meta': {'ordering': "('code',)", 'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'code_slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'credit': ('django.db.models.fields.FloatField', [], {}),
            'cx_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'departments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'course_set'", 'symmetrical': 'False', 'to': "orm['coursesearch.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filled': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grading_style': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'primary_department': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_course_set'", 'null': 'True', 'to': "orm['coursesearch.Department']"}),
            'requirement_areas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'course_set'", 'symmetrical': 'False', 'to': "orm['coursesearch.RequirementArea']"}),
            'spots': ('django.db.models.fields.IntegerField', [], {})
        },
        'coursesearch.department': {
            'Meta': {'object_name': 'Department'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'coursesearch.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'begin': ('django.db.models.fields.TimeField', [], {}),
            'campus': ('django.db.models.fields.SmallIntegerField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coursesearch.Course']"}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            'friday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'monday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wednesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'coursesearch.refreshhistory': {
            'Meta': {'object_name': 'RefreshHistory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_refresh_date': ('django.db.models.fields.DateTimeField', [], {}),
            'run_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'coursesearch.requirementarea': {
            'Meta': {'object_name': 'RequirementArea'},
            'campus': ('django.db.models.fields.SmallIntegerField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'coursesearch.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coursesearch.Course']", 'symmetrical': 'False'}),
            'create_ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['coursesearch']