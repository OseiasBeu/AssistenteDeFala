#-*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='fala_assis',
    version='0.1.1',
    url='https://github.com/mstuttgart/fala_assis',
    license='MIT License',
    author='Oséias Beu',
    author_email='oseiasbeu@outlook.com',
    keywords='Assistente de fala',
    description=u'Assitente de fala qie retorna a execução de uma função para portadores de problemas visuais. Dessa forma, eles poderão saber quando o programa executou',
    packages=['gtts','IPython','time','fala_assis'],
    install_requires=['gtts','IPython'],
)