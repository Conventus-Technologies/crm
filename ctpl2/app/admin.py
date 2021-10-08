from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Company)
class viewproduct(ImportExportModelAdmin):
	list_display=['Company_Name']


@admin.register(Project)
class viewproduct(ImportExportModelAdmin):
	list_display=['Project_Name']


@admin.register(OEM)
class viewproduct(ImportExportModelAdmin):
	list_display=['OEM_Name']


@admin.register(DC)
class viewproduct(ImportExportModelAdmin):
	list_display=['DC_Name']


@admin.register(IR)
class viewproduct(ImportExportModelAdmin):
	list_display=['IR_Name']
	search_display=['Company_Name']
	search_fields=['IR_Name','Company__Company_Name']


@admin.register(BOQ)
class viewproduct(ImportExportModelAdmin):
	list_display=['BOQ_Name']


@admin.register(COP)
class viewproduct(ImportExportModelAdmin):
	list_display=['COP_Name']
	search_fields=['COP_Name','Company__Company_Name']


@admin.register(Product)
class viewproduct(ImportExportModelAdmin):
	list_display=['Customer_Name']


@admin.register(RMA)
class viewproduct(ImportExportModelAdmin):
	list_display=['Customer_name']


@admin.register(RMA_Device)
class viewproduct(ImportExportModelAdmin):
	list_display=['Old_id']