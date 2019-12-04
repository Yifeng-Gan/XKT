# coding: utf-8
# create by tongshiwei on 2019/6/25

from setuptools import setup, find_packages

test_deps = [
    'pytest>=4',
    'pytest-cov>=2.6.0',
    'pytest-pep8>=1',
    'EduData',
    'mxnet',
]

try:
    import mxnet
    mxnet_requires = []
except ModuleNotFoundError:
    mxnet_requires = ["mxnet"]

setup(
    name='XKT',
    version='0.0.1',
    packages=find_packages(),
    python_requires='>=3.6',
    long_description='Refer to full documentation https://github.com/bigdata-ustc/XKT/blob/master/README.md'
                     ' for detailed information.',
    description='This project aims to '
                'provide convenient interfaces for downloading and preprocessing dataset in education.',
    extras_require={
        'test': test_deps,
    },
    install_requires=mxnet_requires + [
        'tqdm',
        'gluonnlp',
        'sklearn',
        'longling>=1.3.0',
    ],  # And any other dependencies foo needs
    entry_points={
        "console_scripts": [
            "DKT = XKT.DKT.DKT:main",
            "DKTVMN = XKT.DKVMN.DKVMN:main"
        ],
    },
)
