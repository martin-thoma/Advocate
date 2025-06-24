import re
import setuptools
from codecs import open

requires = [
    'requests >=2.18.0',
    'urllib3 >=1.22',
    'netifaces>=0.10.5',
]

packages = [
    "advocate",
]

version = ''
with open('advocate/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setuptools.setup(
    name='advocate',
    version=version,
    packages=packages,
    install_requires=requires,
    tests_require=[
        "pytest",
        "pytest-cov",
        "requests-futures",
        "requests-mock",
    ],
    url='https://github.com/JordanMilne/Advocate',
    license='Apache 2',
    author='Jordan Milne',
    author_email='advocate@saynotolinux.com',
    keywords="http requests security ssrf proxy rebinding advocate",
    description=('A wrapper around the requests library for safely '
                 'making HTTP requests on behalf of a third party'),
    long_description=readme,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Security',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
