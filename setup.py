from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/erlendtroite/funniest',
      author='Anders Binders',
      author_email='anders@binders.com',
      license='EAT',
      #packages=['funniest'],
      packages=find_packages(),
      install_requires=[
          'markdown',
      ],
      #dependency_links = ['http://github.com/erlendtroite/funniest/tarball/master#egg=funniest-0.1'],
      include_package_data=True,
      zip_safe=False)
