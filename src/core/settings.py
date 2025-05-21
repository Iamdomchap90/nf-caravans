"""
Django settings for NF caravans.
"""
import os
from pathlib import Path

import dj_database_url
import dj_email_url
import django_cache_url
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from core.widgets import RedactorWidget

PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Set hints to cast the environment variables, and set defaults where necessary.
env = environ.Env(
    DEBUG=(bool, False),
    DEPLOY_ENV=(str, ""),
    PRIMARY_HOST=(str, ""),
    RECAPTCHA_SCORE=(float, 0.7),
    RECAPTCHA_PUBLIC_KEY=(str, ""),
    RECAPTCHA_PRIVATE_KEY=(str, ""),
    REDIS_URL=(str, "redis://cache"),
    EMAIL_URL=(str, "console://"),
    SENTRY_SAMPLE_RATE=(float, 0.1),
    SENTRY_PROFILE_RATE=(float, 0.0),
    SENTRY_URL=(str, ""),
    ALLOWED_HOSTS=(list, ["0.0.0.0", "localhost"]),
    SECRET_KEY=str,
)

# This is what we use to prefix dbs and cache keys etc
DEPLOY_ENV = env("DEPLOY_ENV")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")

PRIMARY_HOST = env("PRIMARY_HOST")

if DEPLOY_ENV != "local":
    RECAPTCHA_REQUIRED_SCORE = env("RECAPTCHA_SCORE")
    RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")

if DEPLOY_ENV not in ["local", "test"]:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    LANGUAGE_COOKIE_HTTPONLY = True
    LANGUAGE_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

ALLOWED_HOSTS += [PRIMARY_HOST]

DATABASES = {"default": dj_database_url.config(conn_max_age=600)}

CSRF_COOKIE_SECURE = False
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True


ADMINS = []
DEFAULT_FROM_EMAIL = "automated@nfcaravans.com"
DEFAULT_TO_EMAIL = ["info@nfcaravans.com"]

CMS_TOOLBAR_ANONYMOUS_ON = False
CMS_ENABLE_UPDATE_CHECK = False
CMS_TEMPLATES = [
    ("base.html", "Default"),
    ("no_breadcrumb.html", "Default (No Breadcrumb)"),
]

ROOT_URLCONF = "core.urls"

WSGI_APPLICATION = "core.wsgi.application"

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
SITE_ID = 1

SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = "SAMEORIGIN"

LANGUAGES = [
    ("en-gb", "English"),
]

DEFAULT_LANGUAGE = "en-gb"

# Cache settings. DOKKU
CACHES = {"default": django_cache_url.parse(env("REDIS_URL"))}

# Storage settings.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Static and Media
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = "/storage/static"
MEDIA_ROOT = "/storage/media"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

email_config = dj_email_url.parse(env("EMAIL_URL"))
vars().update(email_config)

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

if "SENTRY_URL" in os.environ:
    sentry_sdk.init(
        environment=DEPLOY_ENV,
        dsn=env("SENTRY_URL"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=env("SENTRY_SAMPLE_RATE"),
        profiles_sample_rate=env("SENTRY_PROFILE_RATE"),
        send_default_pii=True,
    )

GTM_ID = env("GTM_ID", default="")

if DEPLOY_ENV == "test":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
            "USER": "",
            "PASSWORD": "",
            "HOST": "",
            "PORT": "",
        }
    }
    ROOT_URLCONF = "core.tests.urls"
    GTM_ID = "test_id"

APPS = [
    "users",
    "caravan_bookings",
    "core",
    "news",
    "people",
    "faqs",
    "social_links",
    "footer_links",
]
PLUGINS = [
    "plugins.key_stat",
    "plugins.iframe_embed",
    "plugins.page_cards",
    "plugins.hero_carousel",
    "plugins.gallery",
    "plugins.video",
    "plugins.faq",
    "plugins.rich_text",
    "plugins.people_cards",
    "plugins.article_cards",
]

THIRD_PARTY_APPS = [
    "cms",
    "treebeard",
    "menus",
    "page_extension",
    "sekizai",
    "easy_thumbnails",
    "filer",
    "admin_ordering",
    "admin_extra_buttons",
    "djangocms_admin_style",
    "taggit",
    "import_export",
    "django_q",
    "localflavor",
    "phonenumber_field",
]

DJANGO = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sitemaps",
    "django.contrib.redirects",
]
# Application definition
INSTALLED_APPS = APPS + PLUGINS + THIRD_PARTY_APPS + DJANGO

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "cms.middleware.utils.ApphookReloadMiddleware",
    "core.middleware.DenyIndexMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
                "core.context_processors.sentry_dsn",
                "core.context_processors.sentry_profile_sample_rate",
                "core.context_processors.sentry_replay_session_sample_rate",
                "core.context_processors.sentry_replay_error_sample_rate",
                "footer_links.context_processors.footer_links",
                "social_links.context_processors.social_links",
            ],
            "loaders": ["django.template.loaders.app_directories.Loader"],
            "debug": DEBUG,
        },
    }
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"
FILE_UPLOAD_PERMISSIONS = 0o755
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755
CMS_COLOR_SCHEME_TOGGLE = True
CMS_CONFIRM_VERSION4 = True

# Rich Text settings
WYSIWYG_WIDGET = RedactorWidget
WYSIWYG_CONFIG = {
    "lang": "en",
    "minHeight": "300px",
    "buttons": [
        "html",
        "|",
        "format",
        "|",
        "undo",
        "redo",
        "|",
        "bold",
        "italic",
        "|",
        "ul",
        "ol",
        "|",
        "link",
        "|",
        "sub",
        "sup",
    ],
    "formatting": ["h1", "h2", "h3", "p"],
    "linkTitle": True,
    "linkNewTab": True,
    "structure": True,
    "removeNewLines": True,
    "pasteImages": False,
    "tabAsSpaces": 4,
    "plugins": ["table"],
}

CMS_PLACEHOLDER_CONF = {
    None: {
        "excluded_plugins": ["RelatedArticlePlugin"],
    },
}

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

THUMBNAIL_DEFAULT_OPTIONS = {"crop": True, "upscale": True, "progressive": True}
THUMBNAIL_QUALITY = 80
THUMBNAIL_ALIASES = {
    "": {
        "social_share_image": {"size": (1500, 1000), "crop": False},
        "event:card": {"size": (150, 150), "crop": False},
        "plugins:pullquote": {"size": (150, 150), "crop": False},
        "news:card": {"size": (150, 150), "crop": False},
        "plugins:form_designer": {"size": (150, 150), "crop": False},
        "plugins:gallery:full": {"size": (150, 150), "crop": False},
        "plugins:gallery:thumbnail": {"size": (150, 150), "crop": False},
        "plugins:hero": {"size": (150, 150), "crop": False},
        "plugins:page_card": {"size": (150, 150), "crop": False},
        "plugins:content_width_video": {"size": (150, 150), "crop": False},
        "stories:card_image": {"size": (150, 150), "crop": False},
    },
}

Q_CLUSTER = {
    "name": "nf-caravans",
    "orm": "default",
    "recycle": 100,
    "timeout": 60,
    "retry": 100,
    "max_attempts": 5,
}
