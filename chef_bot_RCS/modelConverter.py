from keras import backend as K
from keras.models import load_model
from freezeGraph import  freeze_session
import tensorflow as tf
# This line must be executed before loading Keras model.
K.set_learning_phase(0)
model = load_model('models/onion.h5')
print(model.outputs)
print(model.inputs)

frozen_graph = freeze_session(K.get_session(),
                              output_names=[out.op.name for out in model.outputs])

tf.train.write_graph(frozen_graph, "model", "onions.pb", as_text=False)