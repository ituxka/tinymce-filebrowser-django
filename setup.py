"""
django-tinymce-filebrowser
-----------------
Simple django-based file uploader and viewer for TinyMCE
"""
from setuptools import setup, find_packages


setup(
    name='Tinymce-filebrowser-django',
    version='1.0.0',
    url='https://github.com/ituxka/django-tinymce-filebrowser',
    license='MIT License',
    author='Nikita Sologub',
    author_email='ituxka@gmail.com',
    description='Django-based file uploader and viewer for TinyMCE',
    keywords="django tinymce fileupload",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'django-tinymce'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)