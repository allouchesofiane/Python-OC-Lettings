"""Migration pour supprimer les anciennes tables de oc_lettings_site."""

from django.db import migrations


class Migration(migrations.Migration):
    """Suppression des anciens modèles après refactorisation."""

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        ('lettings', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(name='Address'),
        migrations.DeleteModel(name='Letting'),
        migrations.DeleteModel(name='Profile'),
    ]