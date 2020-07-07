from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: Apache Software License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='codexpy',
  version='0.0.2',
  description='General use module.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Aryan Kashyap',
  author_email='aryank.kashyap77783@gmail.com',
  license='Apache', 
  classifiers=classifiers,
  keywords='codexpy', 
  packages=find_packages(),
  install_requires=[''] 
)