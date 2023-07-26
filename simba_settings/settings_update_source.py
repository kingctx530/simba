class SettingsUpdateSource:
    def __init__(self):
        self.import_data = [
            'import sys',
            'import os'
        ]

        self.sys_data = ["""
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # 將未來要使用的套件都導入 apps 裡面
PROJECT_NAME = os.path.basename(os.path.dirname(__file__))
"""
        ]

        self.wsgi_data = ["""
WSGI_APPLICATION = "{}.wsgi.application".format(PROJECT_NAME)
"""
        ]

        self.asgi_data = ["""
ASGI_APPLICATION = "{}.asgi.application".format(PROJECT_NAME)
"""
        ]

        self.test_apps_data = ["""
TEST_APP = [

]
"""
        ]

        self.sys_apps_data = ["""
SYS_APP = [
    'calamus',   #auto generate app
]
"""
        ]

        self.installed_apps = ["""
daphne
"""
        ]

        self.install_apps_data = ["""
INSTALLED_APPS = INSTALLED_APPS + SYS_APP + TEST_APP
"""
        ]

        self.template_data = ["""
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
"""
        ]

        self.root_url = ["""
ROOT_URLCONF = '{}.urls'.format(PROJECT_NAME)
"""
        ]

        self.channel_data = ["""
CHANNEL_LAYERS = {
    'default': {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            # "hosts": [('192.168.16.123', '6379')],
            "hosts": [('127.0.0.1', '6379')],
        },
        # "ROUTING": "achilles.channel.routing.channel_routing",
    }
}
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}
"""
                             ]

        self.templatetags = """            #for templatetags use        
            'libraries': {
            },
"""

        self.static_data = """
STATIC_ROOT = (
    os.path.join(BASE_DIR, 'staticfiles')
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'public/static')
]

MEDIA_URL = '/media/'

MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'public/media')
)
"""
        self.other_data = """
#LOGIN_URL = "/admin/login/"
#LOGOUT_REDIRECT_URL  = "/"

# 設定 session 超時時間為 30 分鐘（以秒為單位）
#SESSION_COOKIE_AGE = 1800
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# 用來指定哪些來源的請求會被認為是可信的。這對於防止跨站請求偽造（CSRF）攻擊是非常有用的。
#CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1"],
#CSRF_ALLOWED_ORIGINS = ["http://127.0.0.1"],
#CORS_ORIGINS_WHITELIST = ["http://127.0.0.1"]

# DRF配置，可以不使用
REST_FRAMEWORK = {
    # 全局認證
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # BasicAuthentication:此身份驗證方案使用HTTP基本身份驗證
        # 'rest_framework.authentication.BasicAuthentication',
        # SessionAuthentication:此身份驗證方案使用Django的默認會話後端進行身份驗證
        'rest_framework.authentication.SessionAuthentication',
    ],
    # 全局權限
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',  # 僅通過認證的用戶
        'rest_framework.permissions.AllowAny',  # 允許所有用戶
        #'rest_framework.permissions.IsAdminUser',  # 僅管理員用戶
    ]
}
"""
