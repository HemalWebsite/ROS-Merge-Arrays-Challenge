from setuptools import find_packages, setup

package_name = 'merge_arrays'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hemal Nayyar',
    maintainer_email='hnayyar@wisc.edu',
    description='A ROS 2 node to merge two sorted arrays using dual pointer.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'merge_arrays_node = merge_arrays.index:main',
        ],
    },
)