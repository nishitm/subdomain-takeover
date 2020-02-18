from setuptools import setup

setup(name='subdomain-takeover',
      version='1.0',
      description='Sub-Domain TakeOver Vulnerability Scanner',
      url='https://github.com/nishitm/subdomain-takeover',
      author='nishitm',
      author_email='nishit@mailfence.com',
      license='MIT',
      scripts=['subdomain-takeover.py'],
      install_requires=[
          'requests',
          'urllib3',
      ],
      entry_points={
          'console_scripts': ['subdomain-takeover=subdomain-takeover:main'],
      },
      zip_safe=False)
