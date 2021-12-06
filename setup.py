import setuptools

__version__ = '0.0.1dev1'

# https://github.com/isl-org/DPT
# https://arxiv.org/abs/2103.13413 , "Vision Transformers for Dense Prediction"

setuptools.setup(
    name='dpt',
    version=__version__,
    packages=setuptools.find_packages(),
    # Only put dependencies that's not depends on cuda directly.
    install_requires=['timm']
)
