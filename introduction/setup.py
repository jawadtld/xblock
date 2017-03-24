"""Setup for introduction XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='introduction-xblock',
    version='5.9',
    description='introduction XBlock',   # TODO: write a better description.
    license='UNKNOWN',          # TODO: choose a license: 'AGPL v3' and 'Apache 2.0' are popular.
    packages=[
        'introduction',
    ],
    install_requires=[
        'django >= 1.8, < 1.9',
        'django_nose',
        'mock',
        'coverage',
        'mako',
        'XBlock',
        'xblock-utils',
    ],
    entry_points={
        'xblock.v1': [
            'introduction = introduction:IntroductionXBlock',
        ]
    },
    package_data=package_data("introduction", ["static", "public"]),
)
