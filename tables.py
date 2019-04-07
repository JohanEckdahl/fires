import django_tables2 as tables
from .models import Fire


link = '<a href = "https://kartor.skogsstyrelsen.se/kartorapp/?startapp=skogligagrunddata&x={{record.centerX}}&y={{record.centerY}}&scale=37502.2872&bg=KARTA" target="_blank">Link</a>'


class FireTable(tables.Table):
    link = tables.TemplateColumn(link)
    class Meta:
        model = Fire
        attrs = {'class':'table table-striped'}
        fields = ('number','centerX','centerY', 'link')
