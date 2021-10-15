
import os
import sys
import argparse
from google.protobuf import text_format
import tensorflow as tf


#from tensorflow.core.framework import graph_pb2
#from tensorflow.python.client import session
#from tensorflow.python.framework import importer
#from tensorflow.python.framework import ops
#from tensorflow.python.platform import app
#from tensorflow.python.platform import gfile
#from tensorflow.python.summary import summary

# Silence TensorFlow messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
 
 

def import_to_tensorboard(graph_name, log_dir):
   
  # import meta graph
  tf.compat.v1.train.import_meta_graph(graph_name,clear_devices=True)

  '''
  # traverse graph, node by node
  for n in tf.compat.v1.get_default_graph().as_graph_def().node:
    print(n)
  '''
  
  # create TensorBoard summary file
  with tf.compat.v1.Session() as sess:
    writer = tf.compat.v1.summary.FileWriter(log_dir, sess.graph)
    writer.close()
      
  print("Model Imported. Visualize by running: "
        "tensorboard --logdir={}".format(log_dir))
  print('..or try: `tensorboard --logdir={} --port 6006 --host localhost`'.format(log_dir))
   
  return

   
def run_main():

  # command line argument parsing
  parser = argparse.ArgumentParser(description='Script to import frozen graph into TensorBoard')
  parser.add_argument('-g', '--graph',   type=str, default='', help='Protobuf graph file (.pb) to import into TensorBoard.', required='True')
  parser.add_argument('-l', '--log_dir', type=str, default='tb_log', help='TensorBoard log directory.')
  flags = parser.parse_args()


  print('-------------------------------------')
  print('Input graph:', flags.graph)
  print('Log dir    :', flags.log_dir)
  print('-------------------------------------\n')
  
  
  import_to_tensorboard(flags.graph, flags.log_dir)
  
  return   
   
if __name__ == '__main__':
    run_main()
