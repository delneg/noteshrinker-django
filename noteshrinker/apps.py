from django.apps import AppConfig
from django.conf import settings
import os
class NoteshrinkerConfig(AppConfig):
    name = 'noteshrinker'
    verbose_name = "noteshrinker"
    def ready(self):
        needed_directories = (settings.PNG_ROOT,settings.PDF_ROOT)
        for i in needed_directories:
            if not os.path.isdir(i):
                os.mkdir(i)


