from setuptools import setup


setup(
    name='oem-format-minimize-msgpack',
    version='1.0.0',

    author="Dean Gardiner",
    author_email="me@dgardiner.net",

    install_requires=[
        'oem-framework>=1.0.0',
        'oem-format-minimize>=1.0.0',
        'oem-format-msgpack>=1.0.0'
    ]
)
