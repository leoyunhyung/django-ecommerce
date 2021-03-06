# Generated by Django 3.1.14 on 2022-07-11 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ecommerce.apps.users.models
import ecommerce.bases.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='??????')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='?????????')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='??????')),
                ('phone', ecommerce.apps.users.models.CustomPhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='??????')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '??????',
                'verbose_name_plural': '??????',
            },
            bases=(ecommerce.bases.models.UpdateMixin, models.Model),
            managers=[
                ('objects', ecommerce.apps.users.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserSecession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='??????')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='????????? ??????')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='?????????')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='??????')),
                ('phone', ecommerce.apps.users.models.CustomPhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='??????')),
                ('reason', models.CharField(choices=[('ETC', '??????')], default='ETC', max_length=100, verbose_name='??????')),
            ],
            options={
                'verbose_name': '?????? ??????',
                'verbose_name_plural': '?????? ??????',
            },
            bases=(ecommerce.bases.models.UpdateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='??????')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='????????? ??????')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='??????')),
                ('phone', ecommerce.apps.users.models.CustomPhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='??????')),
                ('total_address', models.CharField(max_length=100, verbose_name='??????')),
                ('main_address', models.CharField(max_length=100, verbose_name='?????? ??????')),
                ('sub_address', models.CharField(max_length=100, verbose_name='?????? ??????')),
                ('postal_code', models.IntegerField(verbose_name='?????? ??????')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL, verbose_name='??????')),
            ],
            options={
                'verbose_name': '?????????',
                'verbose_name_plural': '?????????',
            },
            bases=(ecommerce.bases.models.UpdateMixin, models.Model),
        ),
    ]
