# Generated by Django 3.1.4 on 2021-04-24 04:03

from django.db import migrations, models
import django.utils.timezone
import django_mysql.models
import study_example_app.models.file_field_example_models
import study_example_app.models.normal_field_example_models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_choices_field', models.CharField(choices=[('aaa', '에이에이'), ('bb', '비비')], default='aaa', max_length=128)),
                ('text_choices_field', models.TextField(choices=[('aaa', '에이에이'), ('bb', '비비')], null=True)),
                ('str_field', models.CharField(blank=True, choices=[('aaa', '에이에이'), ('bb', '비비')], db_column='str_field', default='값을 채우지 않으면 이 값을 db을 채운다.', error_messages={'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', 'max_length': 'Ensure this value has at most %(limit_value)d characters (it has %(show_value)d).', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.'}, help_text='주석을 대체하는 Argument다. DB에 영향을 전혀 주지않는다.', max_length=127)),
                ('text_field', django_mysql.models.SizedTextField(blank=True, db_column='text_field', error_messages={'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.'}, size_class=1)),
                ('int_field', models.IntegerField(choices=[(1, '일'), (2, '이'), (3, '삼')], default=0, error_messages={'invalid': "'%(value)s' value must be an integer."}, help_text='주석을 대체하는 Argument다. DB에 영향을 전혀 주지않는다.')),
                ('float_field', models.FloatField()),
                ('decimal_field', models.DecimalField(decimal_places=2, help_text='5(max_digits)개의 자릿수를 저장하고 소숫점2(decimal_places)번째까지 저장 (999.00 ~ 000.00)', max_digits=5)),
                ('bool_field', models.BooleanField(error_messages={'invalid': '“%(value)s” value must be either True or False.', 'invalid_nullable': '“%(value)s” value must be either True, False, or None.'}, help_text="True False 뿐만 아니라 문자열 't' '1'을 True로 인식하고 'f','0'을 False로 인식한다. ")),
                ('date_field', models.DateField(error_messages={'invalid': '“%(value)s” value has an invalid format. It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format.', 'invalid_date': '“%(value)s” value has the correct format (YYYY-MM-DD) but it is an invalid date.'}, help_text='auto_now가 True이면 해당 모델이 .save()될때 마다 최신날짜로 값을 자동으로 갱신해준다.auto_now_add가  True이면 해당모델이 .create()되는 최초1회만 날짜값을 최신날짜를 채워준다.이런 옵션들은 주로 생성날짜, 최근수정날짜를 로깅할때 사용한다.')),
                ('datetime_field', models.DateTimeField(error_messages={'invalid_datetime': '“%(value)s” value has the correct format (YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]) but it is an invalid date/time.'})),
                ('time_field', models.TimeField(default=django.utils.timezone.localtime)),
                ('duration_field', models.DurationField(error_messages={'invalid': '“%(value)s” value has an invalid format. It must be in [DD] [[HH:]MM:]ss[.uuuuuu] format.'}, help_text='python의 timedelta(days=3)를 저장할 수 있다.')),
                ('file_field', models.FileField(max_length=256, upload_to=study_example_app.models.normal_field_example_models.file_upload_to)),
            ],
            options={
                'db_table': 'django_model',
            },
        ),
        migrations.CreateModel(
            name='ExampleUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileFieldExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to=study_example_app.models.file_field_example_models.upload_filepath)),
                ('image', models.ImageField(upload_to=study_example_app.models.file_field_example_models.upload_filepath)),
            ],
        ),
        migrations.CreateModel(
            name='PythonModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_attr', models.CharField(db_column='str_column', default='기본값', max_length=32)),
                ('int_attr', models.IntegerField(db_column='int_column', default=0)),
                ('bool_attr', models.BooleanField(db_column='bool_column', default=False)),
                ('datetime_attr', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'database_table',
            },
        ),
    ]
