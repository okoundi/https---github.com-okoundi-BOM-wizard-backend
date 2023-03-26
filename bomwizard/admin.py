from django.contrib import admin
from . models import *


# Register your models here.
admin.site.register(Project)
admin.site.register(ItemGroup)
admin.site.register(ItemSubGroup)
admin.site.register(StorageArea)
admin.site.register(StorageLocation)
admin.site.register(Item)
admin.site.register(ItemBOM)
admin.site.register(Manual)
admin.site.register(Supplier)
admin.site.register(ItemSupplier)
admin.site.register(Tool)
admin.site.register(FormatRule)
