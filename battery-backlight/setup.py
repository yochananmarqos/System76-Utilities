from setuptools import setup

setup(
    name='s76-battery-backlight',
    version='0.1',
    description='Software to show your battery status with your keyboard backlight',
    url='#',
    author='Jean-François Labonté',
    author_email='grimsleepless@protonmail.com',
    include_package_data=True,
    license='Apache License 2.0',
    packages=['battery_backlight'],
    entry_points={
        'console_scripts': ['battery-backlight=battery_backlight.__main__:main']
    },
)
