#!/usr/bin env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.parameter_descriptions import ParameterValue
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
import os
from pathlib import Path

def generate_launch_description():
    lekiwi_description_dir = get_package_share_directory("lekiwi_description")
    model_arg = DeclareLaunchArgument(
        name="model",
        default_value= os.path.join(lekiwi_description_dir,"urdf","LeKiwi.xacro"),
        description="Path to robot urdf file"
    )
    robot_description =ParameterValue(Command(["xacro ", LaunchConfiguration("model")]),value_type=str)

    robot_state_pub_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description":robot_description}]
    )
    gazebo_resource_path = SetEnvironmentVariable(
        name="GZ_SIM_RESOURCE_PATH",
        value=[
            str(Path(lekiwi_description_dir).parent.resolve())
            ]
        )
    
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory("ros_gz_sim"), "launch"), "/gz_sim.launch.py"]),
                launch_arguments=[
                    ("gz_args", [" -v 4", " -r", " empty.sdf"]
                    )
                ]
             )
    gz_spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=["-topic", "robot_description",
                   "-name", "lekiwi"],
    )

    gz_bridge = Node(
    package="ros_gz_bridge",
    executable="parameter_bridge",
    parameters=[{"config_file": os.path.join(lekiwi_description_dir,"config","ros_gz_bridge.yaml")}],
    output="screen"
        
    )

    rviz_node = Node(

        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=("-d",os.path.join(lekiwi_description_dir,"rviz", "display.rviz"))
    )
    
    return LaunchDescription([
        model_arg,
        gazebo_resource_path,
        robot_state_pub_node,
        gazebo,
        gz_spawn_entity,
        gz_bridge,
        rviz_node,
    ])