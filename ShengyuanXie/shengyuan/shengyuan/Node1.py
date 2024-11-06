#!/usr/bin/env python3
# Note: the file will only save edits in the designated locations
# editable locations are denoted by comments. DO NOT remove the
# generated comments
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8


# add custom imports below

# end custom imports

class Node1(Node):

    def __init__(self):
        super().__init__('node1')
        self.topic1_pub = self.create_publisher(Int8, '/Topic1', 10)

        # customize init function below

        # end init customization




    # add custom methods to the node below

    # end custom methods

def main(args=None):
    # customize main function below
    # Note: editing any of the generated code here could break the node.
    # take precaution when editing
    rclpy.init(args=args)

    node1 = Node1()

    rclpy.spin(node1)

    node1.destroy_node()
    rclpy.shutdown()
    # end main customization


if __name__ == '__main__':
    main()
