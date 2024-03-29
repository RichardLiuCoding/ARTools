from setuptools import setup, find_packages

setup(
  name = 'aespm',
  version = '1.0.0',
  packages = find_packages(),
  package_data = {
    "":["*.txt", "*.mat"]
    },
  include_package_data=True,
  license='MIT',
  description = 'Asylum Research SPM data analysis packages',
  author = 'Richard (Yu) Liu',
  author_email = 'yliu206@utk.edu',
  url = 'https://github.com/RichardLiuCoding/ARTools',
  download_url = 'https://github.com/RichardLiuCoding/ARTools.git',
  keywords = ['SPM', 'AR', 'Python', 'Data Analysis'],
  install_requires=[
          'numpy',
          'scipy',
          'matplotlib',
          'igor2',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
)
