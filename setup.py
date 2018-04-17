from setuptools import setup

setup(name='Correios-sigep',
      version='0.1',
      description='mklace correios sigep integration',
      url='',
      author='Bruno Casado',
      author_email='contato@brunocasado.me',
      license='MIT',
      packages=['correios_sigep', 'correios_sigep.models', 'correios_sigep.utils', 'correios_sigep.reports'],
      install_requires=[
          'lxml',
          'zeep',
          'elaphe',
          'qrcode',
          'pdfkit',
          'candybar'
      ],
      zip_safe=False)
