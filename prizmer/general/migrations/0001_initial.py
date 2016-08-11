# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields

from general.models import Resources, Measurement, TypesMeters, NamesParams, TypesParams, Params, TypesAbonents

def load_resources(apps, schema_editor):
    Resources(guid='06cabd95-80dc-472f-acc7-cad95d4cacb0', name='Холод', type=5).save()
    Resources(guid='44af1849-73b1-4b52-9905-881c8bdb753d', name='Газ', type=6).save()
    Resources(guid='47f0b64c-2bf6-45b4-972b-601f473a3752', name='ХВС', type=2).save()
    Resources(guid='57ec8f42-69c6-4f79-81bb-8ea139407aa9', name='ГВС', type=3).save()
    Resources(guid='ba710cff-e390-48ca-b442-70141c9864f7', name='Электричество', type=1).save()
    Resources(guid='c0491ede-e00b-4e1d-a8ba-1ef61dba1cd3', name='Тепло', type=4).save()
    
def load_measurement(apps, schema_editor):
    Measurement(guid='01bf0015-d0e9-4b10-93ca-89e5a616d31b', name='А', comments='Ампер').save()
    Measurement(guid='06f68849-3e99-4f36-9650-a2687a82f465', name='В', comments='Вольт').save()
    Measurement(guid='146f80c8-b857-4d58-8245-65fb9a8b048e', name='Гц', comments='Герц').save()
    Measurement(guid='1c39318a-806e-461e-b412-38047f9cd265', name='Градус', comments='Градус(угол)').save()
    Measurement(guid='23b35f9b-a699-4bed-be1a-a28e3fd6d55d', name='т', comments='тонна').save()
    Measurement(guid='3006e346-85b4-40a3-ac2f-a63cd0fe5db5', name='м³/ч', comments='метр кубический в час').save()
    Measurement(guid='45162f95-824e-4d88-90ac-6384973c52b8', name='т/ч', comments='тонн в час').save()
    Measurement(guid='78493428-e5ab-49d0-815d-70aede4aa4c2', name='кВА', comments='Киловольт-ампер').save()
    Measurement(guid='903419f1-177e-4881-bdd9-757965bf0757', name='°C', comments='Градус Цельсия').save()
    Measurement(guid='959d5fe1-29fe-441f-988d-4a57543c5232', name='сек.', comments='секунда').save()
    Measurement(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660', name='кВт*ч', comments='Киловатт-час').save()
    Measurement(guid='a9cf9822-3465-4de7-8ff8-10c0395ee29b', name='мин.', comments='минута').save()
    Measurement(guid='abca323e-dc43-4ff3-a6cf-5bc4317dffc8', name='кВар*ч', comments='Киловар-час').save()
    Measurement(guid='c1ebaac1-5aca-4f3e-a560-5c2f67ab7c6e', name='м³', comments='метр кубический').save()
    Measurement(guid='eff414fc-a0cb-4bf9-8ff6-1b0a1711e32d', name='Вт', comments='Ватт').save()
    Measurement(guid='fac1bc47-3c2c-4276-bbae-14dccb5f643a', name='МПа', comments='Мегапаскаль').save()
    
def load_types_meters(apps, schema_editor):
    TypesMeters(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4', name='Меркурий 230', driver_name='m230').save()
    TypesMeters(guid='42e28120-a4a6-4165-85e0-6a675448630a', name='Меркурий 233', driver_name='m233').save()
    TypesMeters(guid='6224d20b-1781-4c39-8799-b1446b60774d', name='Меркурий 200', driver_name='m200').save()
    TypesMeters(guid='66b7ce6a-f280-4e54-8c8d-f69f34aabdf9', name='СЭТ-4ТМ.03М', driver_name='set4tm').save()
    TypesMeters(guid='6d7b64ac-3dba-40d6-8190-d397ae7b9361', name='Пульсар10', driver_name='pulsar10').save()
    TypesMeters(guid='9a4f2233-204d-4ff2-98d7-9d84f34008ee', name='ТЭМ-104', driver_name='tem4').save()
    TypesMeters(guid='baf23191-8b7e-410d-8053-a654c11aaf58', name='Пульсар16', driver_name='pulsar16').save()
    TypesMeters(guid='e8839bfd-af1c-43dd-8c05-5ed0ea61cd6e', name='ПСЧ-3ТА.04', driver_name='psch3ta').save()
    
def load_names_params(apps, schema_editor):
    NamesParams(guid='0136afb0-813f-404d-8857-94226ef82cdb', name='T1 R+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='04edf057-d9ef-46af-b831-6d16d07fb73b', name='T3 R+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='0a8ccd70-bc10-4d7a-a1fd-9226ea0e9db3', name='T2 R+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='0e1b1524-e9d2-4585-a6ee-4c499bdf86e9', name='T0 A+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='1d1d1038-2789-4fcf-a420-8be0ba20d99a', name='T4 A+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='245c6491-d633-4689-94a6-7b3e737ce1e5', name='T0 A-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='338e8dec-c983-4044-bf11-3aa961c5d0a9', name='T0 R-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='390b5791-fe51-4cf9-9103-a9cf446e238e', name='T4 A-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='3aa0b0ca-d62d-497d-a9d5-5d2f7e2d4c67', name='T3 A+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='40e69bf7-fc3f-4a90-8264-988e819a2e9f', name='T0 R+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='6792f35c-8b9d-4b4a-ba0d-33a21e37517f', name='T4 R-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='6e822182-8dca-47f6-a25b-8599423f342e', name='T2 A+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='7257a7d2-a013-4849-88ad-d12a7d9553c5', name='T1 R-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='73209f55-c1b7-460d-b5f6-f376f31a11bf', name='T2 R-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='855aef13-ccb0-4478-ae1e-65d3681e89f6', name='Расход ХВС', guid_resources=Resources.objects.get(guid='47f0b64c-2bf6-45b4-972b-601f473a3752'), guid_measurement=Measurement.objects.get(guid='c1ebaac1-5aca-4f3e-a560-5c2f67ab7c6e')).save()
    NamesParams(guid='885d1ffb-9ad3-4bbf-a3ba-710681c16499', name='T2 A-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='89591d35-2ea7-42f1-ba7d-d08be4d6be1d', name='T1 A-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='93896d3a-b7fb-48fe-8369-7debd6683865', name='T4 R+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='a30f5530-c027-4d8a-815b-6abfb1d81028', name='T1 A+', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='a44a841f-701f-413f-ae53-4a99e29cc52d', name='T3 R-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    NamesParams(guid='fac8bc95-2c22-41a4-b0c6-ccb9b07dc31b', name='T3 A-', guid_resources=Resources.objects.get(guid='ba710cff-e390-48ca-b442-70141c9864f7'), guid_measurement=Measurement.objects.get(guid='a3bf7d60-2b8e-43fc-aae0-c1c66106d660')).save()
    
def load_types_params(apps, schema_editor):
    TypesParams(guid='3242af58-ba57-4d8b-83fa-284bd8f4bd9b', name='Текущий',  period=None, type=0).save()
    TypesParams(guid='3b0d3f12-f92f-476d-96d3-e1d2c1a19e2f', name='Месячный', period=None, type=2).save()
    TypesParams(guid='597eeb75-5d7e-4514-9255-12cc9e6cf97d', name='Архивный', period=None, type=3).save()
    TypesParams(guid='bb986590-63cb-4b9f-8f4b-1b96335c5441', name='Суточный', period=None, type=1).save()
    TypesParams(guid='e78189b5-f9f9-4fdd-830e-5b98c342d7c1', name='Минутный', period=30,   type=4).save()

def load_params(apps, schema_editor):
    Params(guid='06e0a2f0-147f-4b00-9005-9e7941b0036a', param_address=0, channel=3, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='3aa0b0ca-d62d-497d-a9d5-5d2f7e2d4c67'), guid_types_params=TypesParams.objects.get(guid='3242af58-ba57-4d8b-83fa-284bd8f4bd9b')).save()
    Params(guid='11e67353-3ba3-47c3-8667-386346c203a4', param_address=2, channel=0, guid_types_meters=TypesMeters.objects.get(guid='baf23191-8b7e-410d-8053-a654c11aaf58'), guid_names_params=NamesParams.objects.get(guid='855aef13-ccb0-4478-ae1e-65d3681e89f6'), guid_types_params=TypesParams.objects.get(guid='3242af58-ba57-4d8b-83fa-284bd8f4bd9b')).save()
    Params(guid='17789c36-4593-4ff2-94eb-1d0cebdb5366', param_address=0, channel=1, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='a30f5530-c027-4d8a-815b-6abfb1d81028'), guid_types_params=TypesParams.objects.get(guid='3b0d3f12-f92f-476d-96d3-e1d2c1a19e2f')).save()
    Params(guid='37011b85-c8af-4f6c-857d-4b93a95d31e1', param_address=0, channel=2, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='6e822182-8dca-47f6-a25b-8599423f342e'), guid_types_params=TypesParams.objects.get(guid='bb986590-63cb-4b9f-8f4b-1b96335c5441')).save()
    Params(guid='56641ef5-9d6d-48a1-8c37-cab959b3c758', param_address=0, channel=1, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='a30f5530-c027-4d8a-815b-6abfb1d81028'), guid_types_params=TypesParams.objects.get(guid='3242af58-ba57-4d8b-83fa-284bd8f4bd9b')).save()
    Params(guid='5a71b97f-6036-43b1-84df-cf77f9457f20', param_address=1, channel=0, guid_types_meters=TypesMeters.objects.get(guid='baf23191-8b7e-410d-8053-a654c11aaf58'), guid_names_params=NamesParams.objects.get(guid='855aef13-ccb0-4478-ae1e-65d3681e89f6'), guid_types_params=TypesParams.objects.get(guid='bb986590-63cb-4b9f-8f4b-1b96335c5441')).save()
    Params(guid='79741ba9-e8b8-4352-862e-17a9c4d928ce', param_address=0, channel=3, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='3aa0b0ca-d62d-497d-a9d5-5d2f7e2d4c67'), guid_types_params=TypesParams.objects.get(guid='3b0d3f12-f92f-476d-96d3-e1d2c1a19e2f')).save()
    Params(guid='99cd6002-f81c-4ad6-9cb0-53a92a498519', param_address=0, channel=0, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='0e1b1524-e9d2-4585-a6ee-4c499bdf86e9'), guid_types_params=TypesParams.objects.get(guid='bb986590-63cb-4b9f-8f4b-1b96335c5441')).save()
    Params(guid='b2c4b339-0256-4f28-bc5d-92ed78e6d9f7', param_address=0, channel=4, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='1d1d1038-2789-4fcf-a420-8be0ba20d99a'), guid_types_params=TypesParams.objects.get(guid='bb986590-63cb-4b9f-8f4b-1b96335c5441')).save()
    Params(guid='b4c188cb-d57f-44c0-9fe2-fc20deeb74ab', param_address=1, channel=0, guid_types_meters=TypesMeters.objects.get(guid='baf23191-8b7e-410d-8053-a654c11aaf58'), guid_names_params=NamesParams.objects.get(guid='855aef13-ccb0-4478-ae1e-65d3681e89f6'), guid_types_params=TypesParams.objects.get(guid='3242af58-ba57-4d8b-83fa-284bd8f4bd9b')).save()
    Params(guid='b6ceb8d6-fb7d-49c1-95fd-a0ce8303c0df', param_address=0, channel=4, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='1d1d1038-2789-4fcf-a420-8be0ba20d99a'), guid_types_params=TypesParams.objects.get(guid='3b0d3f12-f92f-476d-96d3-e1d2c1a19e2f')).save()
    Params(guid='bdcd1268-37f3-4579-a9d9-5becb2ba8aa3', param_address=0, channel=0, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='0e1b1524-e9d2-4585-a6ee-4c499bdf86e9'), guid_types_params=TypesParams.objects.get(guid='3b0d3f12-f92f-476d-96d3-e1d2c1a19e2f')).save()
    Params(guid='c31297be-220b-4971-8642-6b614aa7ecee', param_address=0, channel=2, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='6e822182-8dca-47f6-a25b-8599423f342e'), guid_types_params=TypesParams.objects.get(guid='3b0d3f12-f92f-476d-96d3-e1d2c1a19e2f')).save()
    Params(guid='c36dcc64-6d02-4957-a931-9d09f87a670d', param_address=2, channel=0, guid_types_meters=TypesMeters.objects.get(guid='baf23191-8b7e-410d-8053-a654c11aaf58'), guid_names_params=NamesParams.objects.get(guid='855aef13-ccb0-4478-ae1e-65d3681e89f6'), guid_types_params=TypesParams.objects.get(guid='bb986590-63cb-4b9f-8f4b-1b96335c5441')).save()
    Params(guid='c3bb9033-ffcb-4a28-91e2-6b45924b8858', param_address=0, channel=3, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='3aa0b0ca-d62d-497d-a9d5-5d2f7e2d4c67'), guid_types_params=TypesParams.objects.get(guid='bb986590-63cb-4b9f-8f4b-1b96335c5441')).save()
    Params(guid='cad09d8d-83fe-441c-8284-848670ca9ca2', param_address=0, channel=2, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='6e822182-8dca-47f6-a25b-8599423f342e'), guid_types_params=TypesParams.objects.get(guid='3242af58-ba57-4d8b-83fa-284bd8f4bd9b')).save()
    Params(guid='cecfa314-8b7b-4bdb-aadf-31444e739fae', param_address=0, channel=4, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='1d1d1038-2789-4fcf-a420-8be0ba20d99a'), guid_types_params=TypesParams.objects.get(guid='3242af58-ba57-4d8b-83fa-284bd8f4bd9b')).save()
    Params(guid='d262c71a-6da4-4ec0-a9c3-b9ea659c246d', param_address=0, channel=1, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='a30f5530-c027-4d8a-815b-6abfb1d81028'), guid_types_params=TypesParams.objects.get(guid='bb986590-63cb-4b9f-8f4b-1b96335c5441')).save()
    Params(guid='e8c20ce7-bdb6-4ea6-8401-cee28049a7d7', param_address=0, channel=0, guid_types_meters=TypesMeters.objects.get(guid='423b33a7-2d68-47b6-b4f6-5b470aedc4f4'), guid_names_params=NamesParams.objects.get(guid='0e1b1524-e9d2-4585-a6ee-4c499bdf86e9'), guid_types_params=TypesParams.objects.get(guid='3242af58-ba57-4d8b-83fa-284bd8f4bd9b')).save()

def load_types_abonents(apps, schema_editor):
    TypesAbonents(guid='01d52a6c-97bb-4e29-ad07-608d449e0ba2', name='АВР').save()
    TypesAbonents(guid='a8c498a7-d7e1-4da7-84a9-d5cb3bac9b7d', name='ОДН').save()
    TypesAbonents(guid='e4d813ca-e264-4579-ae15-385cdbf5d28c', name='Квартиры').save()

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonents',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(max_length=50)),
                ('account_1', models.CharField(max_length=16)),
                ('account_2', models.CharField(max_length=16, blank=True)),
                ('flat_number', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'abonents',
                'verbose_name': '\u0410\u0431\u043e\u043d\u0435\u043d\u0442',
                'verbose_name_plural': '\u0410\u0431\u043e\u043d\u0435\u043d\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BalanceGroups',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'db_table': 'balance_groups',
                'verbose_name': '\u0411\u0430\u043b\u0430\u043d\u0441\u043d\u0430\u044f \u0413\u0440\u0443\u043f\u043f\u0430',
                'verbose_name_plural': '\u0411\u0430\u043b\u0430\u043d\u0441\u043d\u044b\u0435 \u0413\u0440\u0443\u043f\u043f\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComportSettings',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(max_length=3)),
                ('baudrate', models.IntegerField()),
                ('data_bits', models.DecimalField(max_digits=3, decimal_places=0)),
                ('parity', models.DecimalField(max_digits=3, decimal_places=0)),
                ('stop_bits', models.DecimalField(max_digits=3, decimal_places=0)),
                ('write_timeout', models.SmallIntegerField()),
                ('read_timeout', models.SmallIntegerField()),
                ('attempts', models.DecimalField(max_digits=3, decimal_places=0)),
                ('delay_between_sending', models.IntegerField()),
            ],
            options={
                'db_table': 'comport_settings',
                'verbose_name': 'Com \u043f\u043e\u0440\u0442',
                'verbose_name_plural': 'Com \u043f\u043e\u0440\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CurrentValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('value', models.FloatField()),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'current_values',
                'verbose_name': '\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CurrentValuesArchive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('value', models.FloatField()),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'current_values_archive',
                'verbose_name': '\u0410\u0440\u0445\u0438\u0432\u043d\u043e\u0435 \u0442\u0435\u043a\u0443\u0449\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0410\u0440\u0445\u0438\u0432 \u0442\u0435\u043a\u0443\u0449\u0438\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DailyValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('value', models.FloatField()),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'daily_values',
                'verbose_name': '\u0421\u0443\u0442\u043e\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0421\u0443\u0442\u043e\u0447\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkAbonentsTakenParams',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(max_length=50)),
                ('coefficient', models.FloatField(default=1)),
                ('guid_abonents', models.ForeignKey(to='general.Abonents', db_column=b'guid_abonents')),
            ],
            options={
                'db_table': 'link_abonents_taken_params',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u0430 \u043a \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0443',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u043e\u0432 \u043a \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkBalanceGroupsTakenParams',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('type', models.BooleanField(default=True)),
                ('guid_balance_groups', models.ForeignKey(to='general.BalanceGroups', db_column=b'guid_balance_groups')),
            ],
            options={
                'db_table': 'link_balance_groups_taken_params',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0413\u0440\u0443\u043f\u043f \u043a \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0413\u0440\u0443\u043f\u043f \u043a \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkMetersComportSettings',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('guid_comport_settings', models.ForeignKey(to='general.ComportSettings', db_column=b'guid_comport_settings')),
            ],
            options={
                'db_table': 'link_meters_comport_settings',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u0430 \u043a com \u043f\u043e\u0440\u0442\u0443',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u043e\u0432 \u043a com \u043f\u043e\u0440\u0442\u0430\u043c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkMetersTcpipSettings',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
            ],
            options={
                'db_table': 'link_meters_tcpip_settings',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u0430 \u043a tcp/ip \u043f\u043e\u0440\u0442\u0443',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u043e\u0432 \u043a tcp/ip \u043f\u043e\u0440\u0442\u0430\u043c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(unique=True, max_length=50)),
                ('comments', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'measurement',
                'verbose_name': '\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meters',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(unique=True, max_length=50)),
                ('address', models.IntegerField()),
                ('password', models.CharField(max_length=6, blank=True)),
                ('password_type_hex', models.BooleanField(default=True)),
                ('factory_number_manual', models.CharField(max_length=16)),
                ('factory_number_readed', models.CharField(max_length=16, null=True, editable=False, blank=True)),
                ('is_factory_numbers_equal', models.NullBooleanField()),
                ('dt_install', models.DateTimeField(null=True, blank=True)),
                ('dt_last_read', models.DateTimeField(null=True, blank=True)),
                ('time_delay_current', models.IntegerField(default=10)),
                ('guid_meters', models.ForeignKey(db_column=b'guid_meters', blank=True, to='general.Meters', null=True)),
            ],
            options={
                'db_table': 'meters',
                'verbose_name': '\u0421\u0447\u0451\u0442\u0447\u0438\u043a',
                'verbose_name_plural': '\u0421\u0447\u0451\u0442\u0447\u0438\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MonthlyValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('value', models.FloatField()),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'monthly_values',
                'verbose_name': '\u041c\u0435\u0441\u044f\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041c\u0435\u0441\u044f\u0447\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NamesParams',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(unique=True, max_length=50)),
                ('guid_measurement', models.ForeignKey(to='general.Measurement', db_column=b'guid_measurement')),
            ],
            options={
                'db_table': 'names_params',
                'verbose_name': '\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430',
                'verbose_name_plural': '\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(max_length=100)),
                ('level', models.SmallIntegerField()),
                ('guid_parent', models.ForeignKey(db_column=b'guid_parent', blank=True, to='general.Objects', null=True)),
            ],
            options={
                'db_table': 'objects',
                'verbose_name': '\u041e\u0431\u044a\u0435\u043a\u0442',
                'verbose_name_plural': '\u041e\u0431\u044a\u0435\u043a\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Params',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('param_address', models.IntegerField()),
                ('channel', models.IntegerField(default=0)),
                ('guid_names_params', models.ForeignKey(to='general.NamesParams', db_column=b'guid_names_params')),
            ],
            options={
                'db_table': 'params',
                'verbose_name': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440',
                'verbose_name_plural': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(unique=True, max_length=50)),
                ('type', models.DecimalField(unique=True, max_digits=3, decimal_places=0)),
            ],
            options={
                'db_table': 'resources',
                'verbose_name': '\u0420\u0435\u0441\u0443\u0440\u0441',
                'verbose_name_plural': '\u0420\u0435\u0441\u0443\u0440\u0441\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TakenParams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(unique=True, max_length=38, editable=False, name=b'guid', blank=True)),
                ('guid_meters', models.ForeignKey(to='general.Meters', db_column=b'guid_meters')),
                ('guid_params', models.ForeignKey(to='general.Params', db_column=b'guid_params')),
            ],
            options={
                'db_table': 'taken_params',
                'verbose_name': '\u0421\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u043c\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440',
                'verbose_name_plural': '\u0421\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u043c\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcpipSettings',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('ip_address', models.CharField(max_length=15)),
                ('ip_port', models.IntegerField()),
                ('write_timeout', models.SmallIntegerField()),
                ('read_timeout', models.SmallIntegerField()),
                ('attempts', models.DecimalField(max_digits=3, decimal_places=0)),
                ('delay_between_sending', models.IntegerField()),
            ],
            options={
                'db_table': 'tcpip_settings',
                'verbose_name': 'TCP/IP \u043f\u043e\u0440\u0442',
                'verbose_name_plural': 'TCP/IP \u043f\u043e\u0440\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypesAbonents',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'db_table': 'types_abonents',
                'verbose_name': '\u0422\u0438\u043f \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypesMeters',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(unique=True, max_length=50)),
                ('driver_name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'db_table': 'types_meters',
                'verbose_name': '\u0422\u0438\u043f \u0441\u0447\u0451\u0442\u0447\u0438\u043a',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypesParams',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=38, blank=True, name=b'guid')),
                ('name', models.CharField(unique=True, max_length=50)),
                ('period', models.IntegerField(default=0, null=True, blank=True)),
                ('type', models.DecimalField(unique=True, max_digits=3, decimal_places=0)),
            ],
            options={
                'db_table': 'types_params',
                'verbose_name': '\u0422\u0438\u043f \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u043c\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u043c\u044b\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VariousValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('value', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('id_taken_params', models.ForeignKey(to='general.TakenParams', db_column=b'id_taken_params')),
            ],
            options={
                'db_table': 'various_values',
                'verbose_name': '\u041d\u0430\u0441\u0442\u0440\u0430\u0438\u0432\u0430\u0435\u043c\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041d\u0430\u0441\u0442\u0440\u0430\u0438\u0432\u0430\u0435\u043c\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='params',
            name='guid_types_meters',
            field=models.ForeignKey(to='general.TypesMeters', db_column=b'guid_types_meters'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='params',
            name='guid_types_params',
            field=models.ForeignKey(to='general.TypesParams', db_column=b'guid_types_params'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='namesparams',
            name='guid_resources',
            field=models.ForeignKey(to='general.Resources', db_column=b'guid_resources'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthlyvalues',
            name='id_taken_params',
            field=models.ForeignKey(to='general.TakenParams', db_column=b'id_taken_params'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meters',
            name='guid_types_meters',
            field=models.ForeignKey(to='general.TypesMeters', db_column=b'guid_types_meters'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkmeterstcpipsettings',
            name='guid_meters',
            field=models.ForeignKey(to='general.Meters', db_column=b'guid_meters'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkmeterstcpipsettings',
            name='guid_tcpip_settings',
            field=models.ForeignKey(to='general.TcpipSettings', db_column=b'guid_tcpip_settings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkmeterscomportsettings',
            name='guid_meters',
            field=models.ForeignKey(to='general.Meters', db_column=b'guid_meters'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkbalancegroupstakenparams',
            name='id_taken_params',
            field=models.ForeignKey(to='general.TakenParams', db_column=b'id_taken_params'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkabonentstakenparams',
            name='guid_taken_params',
            field=models.ForeignKey(to='general.TakenParams', db_column=b'guid_taken_params', to_field=b'guid'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dailyvalues',
            name='id_taken_params',
            field=models.ForeignKey(to='general.TakenParams', db_column=b'id_taken_params'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='currentvaluesarchive',
            name='id_taken_params',
            field=models.ForeignKey(to='general.TakenParams', db_column=b'id_taken_params'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='currentvalues',
            name='id_taken_params',
            field=models.ForeignKey(to='general.TakenParams', db_column=b'id_taken_params'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='balancegroups',
            name='guid_names_params',
            field=models.ForeignKey(to='general.NamesParams', db_column=b'guid_names_params'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abonents',
            name='guid_objects',
            field=models.ForeignKey(to='general.Objects', db_column=b'guid_objects'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abonents',
            name='guid_types_abonents',
            field=models.ForeignKey(to='general.TypesAbonents', db_column=b'guid_types_abonents'),
            preserve_default=True,
        ),
        migrations.RunPython(load_resources),
        migrations.RunPython(load_measurement),
        migrations.RunPython(load_types_meters),
        migrations.RunPython(load_names_params),
        migrations.RunPython(load_types_params),
        migrations.RunPython(load_params),
        migrations.RunPython(load_types_abonents),
    ]
