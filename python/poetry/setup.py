# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['poetry_demo']

package_data = \
{'': ['*']}

install_requires = \
['ansible>=2.7,<3.0']

setup_kwargs = {
    'name': 'poetry-demo',
    'version': '0.1.0',
    'description': 'poetry demo',
    'long_description': None,
    'author': '10sr',
    'author_email': '8.slashes@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
