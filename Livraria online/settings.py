DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Ou 'django.db.backends.mysql'
        'NAME': 'nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',  # Ou 3306 para MySQL
    }
}
