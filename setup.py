from distutils.core import setup
import sys

setup(
    name='BottleRack',
    version='0.2',
    description='BottleRack Markdown HTML Server',
    author='Steven McGrath',
    author_email='steve@chigeek.com',
    url='https://github.com/SteveMcGrath/bottlerack',
    py_modules=['bottlerack'],
    entry_points = {
        'console_scripts': [
            'bottlerack = bottlerack:main',
            ]
    },
    install_requires=[
        'bottle', 
        'markdown >= 2.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]
)