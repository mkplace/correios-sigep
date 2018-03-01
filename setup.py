from setuptools import setup

setup(name='Correios-sigep',
      version='0.1',
      description='mklace correios sigep integration',
      url='',
      author='Bruno Casado',
      author_email='contato@brunocasado.me',
      license='MIT',
      packages=['correios_sigep'],
      install_requires=[
          'lxml',
          'zeep'
      ],
      zip_safe=False)
