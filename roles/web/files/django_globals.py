{
    'ADMINS': (
        ('PBX admin', 'peter@puptel.net'),
    ),
    'ALLOWED_HOSTS': (
        'pakaa.net',
        'localhost',
    ),
    'INSTALLED_APPS': [
        'django_prometheus',
        'common.apps.CommonConfig',
        'fsapi.apps.FsapiConfig',
        'configuration.apps.ConfigurationConfig',
        'directory.apps.DirectoryConfig',
        'dialplan.apps.DialplanConfig',
        'sofia.apps.SofiaConfig',
        'intercom.apps.IntercomConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ],
    'SERVER_EMAIL': 'noreply@pakaa.net',
    'TIME_ZONE': 'America/Edmonton',
}
