from django.contrib import admin


class MCEFilebrowserAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinymce_filebrowser/js/filebrowser_init.js',)
