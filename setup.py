from setuptools import setup

setup(name='wrightlabutils',
      version='0.1',
      description='Various Utilities for the wright lab',
      url='TBD',
      author='April Wright',
      author_email='april.wright@selu.edu',
      license='MIT',
      packages=['wrightlabutils'],
      install_requires=[
          'dendropy',
          'pandas'
      ],
      long_description=open('README.txt').read(),
      zip_safe=True)

