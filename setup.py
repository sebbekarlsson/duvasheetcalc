from distutils.core import setup
import setuptools


setup(
        name='duvasheetcalc',
        version='2.0',
        install_requires=[
            'openpyxl'
            ],
        packages=[
            'duvasheetcalc'
            ],
        entry_points={
            "console_scripts": [
                "duvasheetcalc = duvasheetcalc.endpoints:calc_sheet"
                ]
            },
        )
