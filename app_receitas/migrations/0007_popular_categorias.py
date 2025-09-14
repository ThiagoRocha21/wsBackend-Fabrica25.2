from django.db import migrations

def criar_categorias(apps, schema_editor):
    Categoria = apps.get_model('app_receitas', 'Categoria')
    categorias = ['Sobremesas', 'Massas', 'Saladas', 'Brasileira', 'Mexicana']
    for nome in categorias:
        Categoria.objects.get_or_create(nome=nome)

class Migration(migrations.Migration):

    dependencies = [
        ('app_receitas', '0001_initial'),  # ou a última migration antes desta
    ]

    operations = [
        migrations.RunPython(criar_categorias),
    ]
