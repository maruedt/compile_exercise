from setuptools import setup
setup(
    name='exercise-compiler',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'compile-exercise=excomp:convert_pynb'
        ]
    }
)