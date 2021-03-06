import tensorflow as tf

class QTargetGraph(object):

    def __init__(self, directory, maze_size):

        self.maze_size = maze_size
        tf.reset_default_graph()
        self.graph = tf.Graph()

        with self.graph.as_default():
            saver = tf.train.import_meta_graph(directory + ".meta")
            self.logits = tf.get_collection('logits')

        self.sess = tf.Session(graph=self.graph)
        saver.restore(self.sess, directory)


    def GetActionValues(self, X):

        preds = self.sess.run(self.logits, feed_dict={'X:0': X / self.maze_size})

        return preds










