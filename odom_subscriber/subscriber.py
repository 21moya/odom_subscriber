import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry

class Subscriber(Node):

    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            '/rosbot_base_controller/odom',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('I heeard: "%s"' % msg.data)
        with open("odom.txt", "a") as f:
            f.write(f"{msg.pose.pose.position.x} {msg.pose.pose.position.y}")
        f.close()

def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
