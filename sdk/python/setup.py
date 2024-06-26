# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = "0.0.0"
def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "twingate Pulumi Package - Development Version"


setup(name='emailbob_twingate',
      python_requires='>=3.8',
      version=VERSION,
      description="A Pulumi package for creating and managing Twingate cloud resources.",
      long_description=readme(),
      long_description_content_type='text/markdown',
      keywords='pulumi twingate category/infrastructure',
      url='https://www.twingate.com',
      project_urls={
          'Repository': 'https://github.com/emailbob/pulumi-twingate'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'emailbob_twingate': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0,<4.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
