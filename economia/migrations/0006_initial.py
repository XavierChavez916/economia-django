# Generated by Django 4.1.3 on 2023-01-31 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('economia', '0005_delete_indicadorambiental_delete_indicadoreconomico_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('idMunicipios', models.IntegerField(default='some_value', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=45, null=True)),
                ('usuario', models.CharField(blank=True, max_length=45, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('contrasenia', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndicadorSocial',
            fields=[
                ('id_social', models.IntegerField(primary_key=True, serialize=False)),
                ('porcentaje_barrido_rurales', models.IntegerField(null=True)),
                ('num_vehiculos', models.IntegerField(null=True)),
                ('capacidad_tone_vehiculos', models.IntegerField(null=True)),
                ('porcentaje_barrido', models.IntegerField(null=True)),
                ('km_barrido', models.IntegerField(null=True)),
                ('porcentaje_barrido_urbanas', models.IntegerField(null=True)),
                ('porcentaje_residuos', models.IntegerField(null=True)),
                ('proyectos_conservacion_agua', models.IntegerField(null=True)),
                ('abast_agua_horas', models.IntegerField(null=True)),
                ('area_m2_institucion', models.IntegerField(null=True)),
                ('area_m2_parques', models.IntegerField(null=True)),
                ('area_m2_plazas', models.IntegerField(null=True)),
                ('area_m2_jardines', models.IntegerField(null=True)),
                ('area_m2_parterres', models.IntegerField(null=True)),
                ('area_m2_riberas', models.IntegerField(null=True)),
                ('area_m2_estadios', models.IntegerField(null=True)),
                ('area_m2_canchas', models.IntegerField(null=True)),
                ('area_m2_urbanas', models.IntegerField(null=True)),
                ('area_total_hect', models.IntegerField(null=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='economia.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='IndicadorInstitucional',
            fields=[
                ('id_institucional', models.IntegerField(primary_key=True, serialize=False)),
                ('funcionarios_tiempo_completo', models.IntegerField(null=True)),
                ('cobertura_km_barrido_publicas', models.IntegerField(null=True)),
                ('personas_servicio_barrido', models.IntegerField(null=True)),
                ('personas_gestion_ambiental', models.IntegerField(null=True)),
                ('energia_kWh', models.IntegerField(null=True)),
                ('energia_valor', models.IntegerField(null=True)),
                ('combustible_diesel', models.IntegerField(null=True)),
                ('combustible_extra', models.IntegerField(null=True)),
                ('combustible_super', models.IntegerField(null=True)),
                ('num_productos', models.IntegerField(null=True)),
                ('num_cortes_servicio', models.IntegerField(null=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='economia.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='IndicadorEconomico',
            fields=[
                ('id_economico', models.IntegerField(primary_key=True, serialize=False)),
                ('presupuesto_anual', models.IntegerField(null=True)),
                ('monto_residencial', models.IntegerField(null=True)),
                ('monto_residencial_industrial', models.IntegerField(null=True)),
                ('presupuesto_campañas', models.IntegerField(null=True)),
                ('ingresos_fiscales', models.IntegerField(null=True)),
                ('ingresos_preasignaciones', models.IntegerField(null=True)),
                ('ingresos_credito', models.IntegerField(null=True)),
                ('ingresos_asistencia', models.IntegerField(null=True)),
                ('ingresos_anticipos', models.IntegerField(null=True)),
                ('ingresos_totales', models.IntegerField(null=True)),
                ('ingresos_ambiental_fiscales', models.IntegerField(null=True)),
                ('ingresos_ambiental_preasignaciones', models.IntegerField(null=True)),
                ('ingresos_totales_ambiental', models.IntegerField(null=True)),
                ('municipio', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='economia.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='IndicadorAmbiental',
            fields=[
                ('id_ambiental', models.IntegerField(primary_key=True, serialize=False)),
                ('area_sanitarios', models.IntegerField(null=True)),
                ('num_botaderos', models.IntegerField(null=True)),
                ('total_residuos_tone', models.IntegerField(null=True)),
                ('total_residuos_solidos', models.IntegerField(null=True)),
                ('total_residuos_peligroso_ton', models.IntegerField(null=True)),
                ('total_residuos_organicos_ton', models.IntegerField(null=True)),
                ('total_residuos_inorganicos_ton', models.IntegerField(null=True)),
                ('total_residuos', models.IntegerField(null=True)),
                ('residuos_urbanos_reciclaje', models.IntegerField(null=True)),
                ('total_residuos_urbanos', models.IntegerField(null=True)),
                ('total_residuos_solidos_peligrososo', models.IntegerField(null=True)),
                ('captacion_agua_superficial', models.IntegerField(null=True)),
                ('captacion_agua_subterranea', models.IntegerField(null=True)),
                ('volumen_total_superficial_subterranea', models.IntegerField(null=True)),
                ('volumen_bruto_dulce', models.IntegerField(null=True)),
                ('volumen_agua_usuario', models.IntegerField(null=True)),
                ('total_agua_residual_recolectada', models.IntegerField(null=True)),
                ('total_residual_tratamiento', models.IntegerField(null=True)),
                ('num_plantas_tratamiento_residual', models.IntegerField(null=True)),
                ('capacidad_tratamiento_residual', models.IntegerField(null=True)),
                ('total_agua_notratada_m3', models.CharField(max_length=45, null=True)),
                ('total_agua_tratada_vertida', models.CharField(max_length=45, null=True)),
                ('total_agua_no_tratada_vertida', models.CharField(max_length=45, null=True)),
                ('catidad_agua_residual_alcatarillado_m3', models.CharField(max_length=45, null=True)),
                ('consumo_agua', models.CharField(max_length=45, null=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='economia.municipio')),
            ],
        ),
    ]