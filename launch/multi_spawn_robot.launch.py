#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, TextSubstitution



def gen_robot_list(number_of_robots):

    robots = []

    for i in range(number_of_robots):
        robot_name = "b_rover"+str(i)
        x_pos = float(i)
        y_pos = float(i)
        robots.append({'name': robot_name, 'x_pose': x_pos, 'y_pose': y_pos, 'z_pose': 0.01})


    return robots 

def generate_launch_description():

    sdf = os.path.join(get_package_share_directory('b_rover_description'), 'models/b_rover/', 'model.sdf')
    pkg_b_rover_description = get_package_share_directory('b_rover_description')
    assert os.path.exists(sdf), "model.sdf doesnt exist in "+str(sdf)

    # Names and poses of the robots
    robots = gen_robot_list(6)

    # We create the list of spawn robots commands
    spawn_robots_cmds = []
    for robot in robots:
        spawn_robots_cmds.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(pkg_b_rover_description, 'launch',
                                                           'spawn_b_rover.launch.py')),
                launch_arguments={
                                  'robot_sdf': sdf,
                                  'x': TextSubstitution(text=str(robot['x_pose'])),
                                  'y': TextSubstitution(text=str(robot['y_pose'])),
                                  'z': TextSubstitution(text=str(robot['z_pose'])),
                                  'robot_name': robot['name'],
                                  'robot_namespace': robot['name']
                                  }.items()))

    # Create the launch description and populate
    ld = LaunchDescription()
    
    for spawn_robot_cmd in spawn_robots_cmds:
        ld.add_action(spawn_robot_cmd)

    return ld
