from setuptools import setup

setup(
    # Needed to silence warnings
    name='planet_utils',
    url='https://github.com/ankurk017/planet_utils',
    author='Ankur Kumar',
    author_email='ankurk017@gmail.com',
    # Needed to actually package something
    packages=['planet_utils'],
    # Needed for dependencies
    install_requires=["cartopy", "matplotlib", "numpy", "xarray"],
    # *strongly* suggested for sharing
    version='0.1',
    license='MIT',
    description='Planet Utilities',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.rst').read(),
    # if there are any scripts
    scripts=['scripts/hello.py'],
)
