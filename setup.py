from setuptools import find_packages, setup

from netbox_nagios.version import VERSION

setup(
    name="netbox-nagios",
    version=VERSION,
    author="Gabriel KAHLOUCHE",
    author_email="gabriel.kahlouche@groupama.com",
    description="Netbox Plugin to show centreon device state in Netbox.",
    url="https://github.com/jessux/netbox-nagios",
    license="",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
