from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='shengyuan_xie',
            executable='node1',
            name='node1'
        ),

        # customize launch file below

        # end launch file customization
    ])
