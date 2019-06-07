import django_tables2 as tables
from .models import Fire


link = '<a href = "https://kartor.skogsstyrelsen.se/kartorapp/?startapp=skogligagrunddata&x={{record.CenterX}}&y={{record.CenterY}}&scale=37502.2872&bg=KARTA" target="_blank">Link</a>'



class FireTable(tables.Table):
    link = tables.TemplateColumn(link)
    class Meta:
        model = Fire
        attrs = {'class':'table table-striped'}
        fields = ('OBJECTID','GISHektar', 'CenterX','CenterY', 'link')


class SkogsstyrelsenTable(tables.Table):
    link = tables.TemplateColumn(link)
    class Meta:
        model = Fire
        attrs = {'class':'table table-striped'}
        fields = ('NAMN', 'Producent', 'GISHektar', 'Lannamn', 'CenterX', 'CenterY',
                'Aktualitet', 'Kommunnamn', 'Metod', 'Kvalitet', 'Kommentar',
                'OBJECTID', 'Laddatum', 'Lopnr', 'shape_STAr', 'shape_STLe')

