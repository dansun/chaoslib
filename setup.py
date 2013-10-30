from setuptools import setup

setup(name='chaoslib',
      version='0.1',
      description='Sorting library for chaossort.',
      url='http://github.com/dansun/chaossort',
      author='Daniel Sundberg',
      author_email='daniel@danielsundberg.nu',
      license='Apache License Version 2.00',
      packages=['chaoslib'],
      install_requires=['randomdotorg'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
