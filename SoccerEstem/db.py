MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd_soccerestem',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost', 
        'PORT': '3306',
				'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}







