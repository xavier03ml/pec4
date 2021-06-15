from setuptools import setup

setup(
    name='covid_approval_checker',
    version='0.0.1',    
    description='Proyecto de creacón de un paquete Python para la tarea PEC 4',
    url='https://github.com/xavier03ml/pec4',
    author='Xavier Merchán',
    author_email='xaviermerchan1989@gmail.com',
    license='MIT',
    packages=['covid_approval_checker'],
    install_requires=['pandas>=1.2.4',
                      'matplotlib>=3.0',                     
                      ],

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)