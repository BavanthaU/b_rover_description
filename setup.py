
import os # Operating system library
from glob import glob # Handles file path names
from setuptools import setup # Facilitates the building of packages

package_name = 'b_rover_description'

# Path of the current directory
cur_directory_path = os.path.abspath(os.path.dirname(__file__))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Path to the launch file      
        (os.path.join('share', package_name,'launch'), glob('launch/*.launch.py')),

        # Path to the world file
        (os.path.join('share', package_name,'worlds/'), glob('./worlds/*')),

        (os.path.join('share', package_name,'models/b_rover/meshes'), glob('./models/b_rover/meshes/*')),

        # Path to the mobile robot sdf file
        (os.path.join('share', package_name,'models/b_rover/'), glob('./models/b_rover/model.*')),

        # Path to the world file (i.e. warehouse + global environment)
        (os.path.join('share', package_name,'models/'), glob('./worlds/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bavantha',
    maintainer_email='bavanthau@eng.pdn.ac.lk',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'b_rover_demo = b_rover_description.b_rover_demo:main'
        ],
    },
)

