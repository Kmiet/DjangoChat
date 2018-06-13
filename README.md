# DjangoChat
Simple chat app written in Django using Django-Channels. It is based mostly on their tutorials.

## Tech
#
| Framework |   |
| ------ | ------ |
| Django | [Django] |
| Django-Channels | [Django-Channels] |
| Redis | [Redis] |

#
#### Installation

Download dependencies using PIP:
```sh
$ pip install django
$ pip install channels
$ pip install channels-redis
```

#### 'Secret' settings

Put your secret.py file in DjangoChat directory. 

#
```py
#Database
DB_SETUP = {
    'default': {
        #Follow the instructions in Django Docs
        'ENGINE': 'django.db.backends.(YOUR_DB_ENGINE_CHECK_DJANGO_DOCS)',
        'NAME': 'YOUR_DATABASE_NAME',
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'YOUR_PASSWORD',
        'HOST': 'YOUR_DB_HOST_ADDR',
        'PORT': 'YOUR_DB_HOST_PORT',
    }
}

#Hosts (i.e. your domain)
HOSTS = [
	'YOUR_DOMAIN_OTHERWISE_NONE_CHECK_DJANGO_DOCS',
]

#Channel Layer for Django Channels
CH_LAYERS = {
    'default': {
        #For example Redis
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            #Redis host
            "hosts": [('REDIS_HOST_ADDR', REDIS_HOST_PORT)],
        },
    },
}

#Read Django Docs
SEC_KEY = 'YOUR_DJANGO_PROJ_SECRET_KEY'
```
#


   [Django]: <https://www.djangoproject.com/>
   [Django-Channels]: <https://channels.readthedocs.io/>
   [Redis]: <https://redis.io/>