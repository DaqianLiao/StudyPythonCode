
import tensorflow as tf

# 定义一个常量
hello = tf.constant('Hello, TensorFlow!')

# Start tf session 启动一个tf session
sess = tf.Session()

# Run the op 运行结果
print(sess.run(hello))
# 需要显示的关闭session
sess.close()