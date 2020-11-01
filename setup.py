"""This module contains the packaging routine for the ``scrapy-algolia-exporter`` package"""

from setuptools import setup, find_packages

try:  # pip >= 10
    from pip._internal.req import parse_requirements

    try:
        from pip._internal.download import PipSession
    except ImportError:  # pip >= 20
        from pip._internal.network.session import PipSession

    pip_session = PipSession()
except ImportError:  # pip <= 9.0.3
    from pip.req import parse_requirements

    try:
        from pip.download import PipSession
        pip_session = PipSession()
    except ImportError:  # backup
        pip_session = 'hack'


def get_requirements(source):
    """Get the requirements from the given ``source``

    Parameters
    ----------
    source: str
        The filename containing the requirements

    """

    install_reqs = parse_requirements(filename=source, session=pip_session)

    try:
        return [str(ir.req) for ir in install_reqs]
    except AttributeError:  # pip >= 10
        return [str(ir.requirement) for ir in install_reqs]


setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
