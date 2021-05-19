tinymce-filebrowser-django
===

**tinymce-filebrowser-django** is a simple and flexible tool for managing your files and images from TinyMCE editor.

Quickstart:
===

Install tinymce-filebrowser-django:

    $ pip install tinymce-filebrowser-django

Add tinymce and tinymce_filebrowser to INSTALLED_APPS in settings.py for your project:

    INSTALLED_APPS = (
        ...
        'tinymce',
        'tinymce_filebrowser',
    )

Migrate tinymce-filebrowser-django models
    
    $ python manage.py migrate tinymce_filebrowser
    
Change tinymce config to work with filebrowser:

    TINYMCE_DEFAULT_CONFIG = {
      'file_browser_callback': 'tinymce_filebrowser'
    }

Add tinymce_filebrowser.urls to urls.py for your project:

    urlpatterns = [
        ...
        url(r'^tinymce/', include('tinymce.urls')),
        url(r'^tinymce_filebrowser/', include('tinymce_filebrowser.urls')),
    ]

In your models.py code:

    from django.db import models
    from tinymce.models import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField()
        
In your admin.py:

    from django.contrib import admin
    from myapp.models import MyModel
    from tinymce_filebrowser.admin import MCEFilebrowserAdmin

    class MyModelAdmin(MCEFilebrowserAdmin):
        pass

    admin.site.register(MyModel, MyModelAdmin)

**tinymce-filebrowser-django** uses django staticfiles.


If You do not use django-tinymce package then add next lines to TinyMCE init:

    tinyMCE.init({
        ...
        "file_browser_callback": "tinymce_filebrowser"
    })
    

Additional settings:

    FILEBROWSER_PER_PAGE - files per page in filebrowser
