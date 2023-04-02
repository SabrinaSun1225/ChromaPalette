from setuptools import setup, find_packages

setup(
    name='ChromaPalette',
    version='0.1.0',
    description='A Versatile Scientific Color Palette Library',

    author='Sabrina Sun',
    author_email='sabrinasun1225@outlook.com',
    license='MIT',
    url='https://github.com/SabrinaSun1225/ChromaPalette',
    
    packages=find_packages(),

    install_requires=[
        'numpy',
        'scipy'
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    include_package_data=True,
    package_data={'ChromaPalette': ['ColorBars.csv']}
)
