# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""MobileNet v1.

MobileNet is a general architecture and can be used for multiple use cases.
Depending on the use case, it can use different input layer size and different
head (for example: embeddings, localization and classification).

As described in https://arxiv.org/abs/1704.04861.

  MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications
  Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam

100% Mobilenet V1 (base) with input size 224x224:

See mobilenet_v1()

Layer                                                     params           macs
--------------------------------------------------------------------------------
MobilenetV1/Conv2d_0/Conv2D:                                 864      10,838,016
MobilenetV1/Conv2d_1_depthwise/depthwise:                    288       3,612,672
MobilenetV1/Conv2d_1_pointwise/Conv2D:                     2,048      25,690,112
MobilenetV1/Conv2d_2_depthwise/depthwise:                    576       1,806,336
MobilenetV1/Conv2d_2_pointwise/Conv2D:                     8,192      25,690,112
MobilenetV1/Conv2d_3_depthwise/depthwise:                  1,152       3,612,672
MobilenetV1/Conv2d_3_pointwise/Conv2D:                    16,384      51,380,224
MobilenetV1/Conv2d_4_depthwise/depthwise:                  1,152         903,168
MobilenetV1/Conv2d_4_pointwise/Conv2D:                    32,768      25,690,112
MobilenetV1/Conv2d_5_depthwise/depthwise:                  2,304       1,806,336
MobilenetV1/Conv2d_5_pointwise/Conv2D:                    65,536      51,380,224
MobilenetV1/Conv2d_6_depthwise/depthwise:                  2,304         451,584
MobilenetV1/Conv2d_6_pointwise/Conv2D:                   131,072      25,690,112
MobilenetV1/Conv2d_7_depthwise/depthwise:                  4,608         903,168
MobilenetV1/Conv2d_7_pointwise/Conv2D:                   262,144      51,380,224
MobilenetV1/Conv2d_8_depthwise/depthwise:                  4,608         903,168
MobilenetV1/Conv2d_8_pointwise/Conv2D:                   262,144      51,380,224
MobilenetV1/Conv2d_9_depthwise/depthwise:                  4,608         903,168
MobilenetV1/Conv2d_9_pointwise/Conv2D:                   262,144      51,380,224
MobilenetV1/Conv2d_10_depthwise/depthwise:                 4,608         903,168
MobilenetV1/Conv2d_10_pointwise/Conv2D:                  262,144      51,380,224
MobilenetV1/Conv2d_11_depthwise/depthwise:                 4,608         903,168
MobilenetV1/Conv2d_11_pointwise/Conv2D:                  262,144      51,380,224
MobilenetV1/Conv2d_12_depthwise/depthwise:                 4,608         225,792
MobilenetV1/Conv2d_12_pointwise/Conv2D:                  524,288      25,690,112
MobilenetV1/Conv2d_13_depthwise/depthwise:                 9,216         451,584
MobilenetV1/Conv2d_13_pointwise/Conv2D:                1,048,576      51,380,224
--------------------------------------------------------------------------------
Total:                                                 3,185,088     567,716,352


75% Mobilenet V1 (base) with input size 128x128:

See mobilenet_v1_075()

Layer                                                     params           macs
--------------------------------------------------------------------------------
MobilenetV1/Conv2d_0/Conv2D:                                 648       2,654,208
MobilenetV1/Conv2d_1_depthwise/depthwise:                    216         884,736
MobilenetV1/Conv2d_1_pointwise/Conv2D:                     1,152       4,718,592
MobilenetV1/Conv2d_2_depthwise/depthwise:                    432         442,368
MobilenetV1/Conv2d_2_pointwise/Conv2D:                     4,608       4,718,592
MobilenetV1/Conv2d_3_depthwise/depthwise:                    864         884,736
MobilenetV1/Conv2d_3_pointwise/Conv2D:                     9,216       9,437,184
MobilenetV1/Conv2d_4_depthwise/depthwise:                    864         221,184
MobilenetV1/Conv2d_4_pointwise/Conv2D:                    18,432       4,718,592
MobilenetV1/Conv2d_5_depthwise/depthwise:                  1,728         442,368
MobilenetV1/Conv2d_5_pointwise/Conv2D:                    36,864       9,437,184
MobilenetV1/Conv2d_6_depthwise/depthwise:                  1,728         110,592
MobilenetV1/Conv2d_6_pointwise/Conv2D:                    73,728       4,718,592
MobilenetV1/Conv2d_7_depthwise/depthwise:                  3,456         221,184
MobilenetV1/Conv2d_7_pointwise/Conv2D:                   147,456       9,437,184
MobilenetV1/Conv2d_8_depthwise/depthwise:                  3,456         221,184
MobilenetV1/Conv2d_8_pointwise/Conv2D:                   147,456       9,437,184
MobilenetV1/Conv2d_9_depthwise/depthwise:                  3,456         221,184
MobilenetV1/Conv2d_9_pointwise/Conv2D:                   147,456       9,437,184
MobilenetV1/Conv2d_10_depthwise/depthwise:                 3,456         221,184
MobilenetV1/Conv2d_10_pointwise/Conv2D:                  147,456       9,437,184
MobilenetV1/Conv2d_11_depthwise/depthwise:                 3,456         221,184
MobilenetV1/Conv2d_11_pointwise/Conv2D:                  147,456       9,437,184
MobilenetV1/Conv2d_12_depthwise/depthwise:                 3,456          55,296
MobilenetV1/Conv2d_12_pointwise/Conv2D:                  294,912       4,718,592
MobilenetV1/Conv2d_13_depthwise/depthwise:                 6,912         110,592
MobilenetV1/Conv2d_13_pointwise/Conv2D:                  589,824       9,437,184
--------------------------------------------------------------------------------
Total:                                                 1,800,144     106,002,432

"""

# Tensorflow mandates these.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# From this repo
from mobilenet.fileio import get_logger
from mobilenet.imagenet import load_imagenet_labels
from mobilenet.toco import toco_convert, FLOAT, QUANTIZED_UINT8

from scipy.misc import imread, imresize
import numpy as np

from collections import namedtuple
import functools
import time
import os

from tensorflow.python.framework import graph_util
import tensorflow as tf

slim = tf.contrib.slim

# Conv and DepthSepConv namedtuple define layers of the MobileNet architecture
# Conv defines 3x3 convolution layers
# DepthSepConv defines 3x3 depthwise convolution followed by 1x1 convolution.
# stride is the stride of the convolution
# depth is the number of channels or filters in a layer
Conv = namedtuple('Conv', ['kernel', 'stride', 'depth'])
DepthSepConv = namedtuple('DepthSepConv', ['kernel', 'stride', 'depth'])

# _CONV_DEFS specifies the MobileNet body
_CONV_DEFS = [
    Conv(kernel=[3, 3], stride=2, depth=32),
    DepthSepConv(kernel=[3, 3], stride=1, depth=64),
    DepthSepConv(kernel=[3, 3], stride=2, depth=128),
    DepthSepConv(kernel=[3, 3], stride=1, depth=128),
    DepthSepConv(kernel=[3, 3], stride=2, depth=256),
    DepthSepConv(kernel=[3, 3], stride=1, depth=256),
    DepthSepConv(kernel=[3, 3], stride=2, depth=512),
    DepthSepConv(kernel=[3, 3], stride=1, depth=512),
    DepthSepConv(kernel=[3, 3], stride=1, depth=512),
    DepthSepConv(kernel=[3, 3], stride=1, depth=512),
    DepthSepConv(kernel=[3, 3], stride=1, depth=512),
    DepthSepConv(kernel=[3, 3], stride=1, depth=512),
    DepthSepConv(kernel=[3, 3], stride=2, depth=1024),
    DepthSepConv(kernel=[3, 3], stride=1, depth=1024)
]


def mobilenet_v1_base(inputs,
                      final_endpoint='Conv2d_13_pointwise',
                      min_depth=8,
                      depth_multiplier=1.0,
                      conv_defs=None,
                      output_stride=None,
                      scope=None):
    """Mobilenet v1.

    Constructs a Mobilenet v1 network from inputs to the given final endpoint.

    Args:
    inputs: a tensor of shape [batch_size, height, width, channels].
    final_endpoint: specifies the endpoint to construct the network up to. It
      can be one of ['Conv2d_0', 'Conv2d_1_pointwise', 'Conv2d_2_pointwise',
      'Conv2d_3_pointwise', 'Conv2d_4_pointwise', 'Conv2d_5_pointwise',
      'Conv2d_6_pointwise', 'Conv2d_7_pointwise', 'Conv2d_8_pointwise',
      'Conv2d_9_pointwise', 'Conv2d_10_pointwise', 'Conv2d_11_pointwise',
      'Conv2d_12_pointwise', 'Conv2d_13_pointwise'].
    min_depth: Minimum depth value (number of channels) for all convolution ops.
      Enforced when depth_multiplier < 1, and not an active constraint when
      depth_multiplier >= 1.
    depth_multiplier: Float multiplier for the depth (number of channels)
      for all convolution ops. The value must be greater than zero. Typical
      usage will be to set this value in (0, 1) to reduce the number of
      parameters or computation cost of the model.
    conv_defs: A list of ConvDef namedtuples specifying the net architecture.
    output_stride: An integer that specifies the requested ratio of input to
      output spatial resolution. If not None, then we invoke atrous convolution
      if necessary to prevent the network from reducing the spatial resolution
      of the activation maps. Allowed values are 8 (accurate fully convolutional
      mode), 16 (fast fully convolutional mode), 32 (classification mode).
    scope: Optional variable_scope.

    Returns:
    tensor_out: output tensor corresponding to the final_endpoint.
    end_points: a set of activations for external use, for example summaries or
                losses.

    Raises:
    ValueError: if final_endpoint is not set to one of the predefined values,
                or depth_multiplier <= 0, or the target output_stride is not
                allowed.
    """
    depth = lambda d: max(int(d * depth_multiplier), min_depth)
    end_points = {}

    # Used to find thinned depths for each layer.
    if depth_multiplier <= 0:
        raise ValueError('depth_multiplier is not greater than zero.')

    if conv_defs is None:
        conv_defs = _CONV_DEFS

    if output_stride is not None and output_stride not in [8, 16, 32]:
        raise ValueError('Only allowed output_stride values are 8, 16, 32.')

    with tf.variable_scope(scope, 'MobilenetV1', [inputs]):
        with slim.arg_scope([slim.conv2d, slim.separable_conv2d], padding='SAME'):
            # The current_stride variable keeps track of the output stride of the
            # activations, i.e., the running product of convolution strides up to the
            # current network layer. This allows us to invoke atrous convolution
            # whenever applying the next convolution would result in the activations
            # having output stride larger than the target output_stride.
            current_stride = 1

            # The atrous convolution rate parameter.
            rate = 1

            net = inputs
            for i, conv_def in enumerate(conv_defs):
                end_point_base = 'Conv2d_%d' % i

                if output_stride is not None and current_stride == output_stride:
                    # If we have reached the target output_stride, then we need to employ
                    # atrous convolution with stride=1 and multiply the atrous rate by the
                    # current unit's stride for use in subsequent layers.
                    layer_stride = 1
                    layer_rate = rate
                    rate *= conv_def.stride
                else:
                    layer_stride = conv_def.stride
                    layer_rate = 1
                    current_stride *= conv_def.stride

                if isinstance(conv_def, Conv):
                    end_point = end_point_base
                    net = slim.conv2d(net, depth(conv_def.depth), conv_def.kernel,
                                      stride=conv_def.stride,
                                      normalizer_fn=slim.batch_norm,
                                      scope=end_point)
                    end_points[end_point] = net
                    if end_point == final_endpoint:
                        return net, end_points

                elif isinstance(conv_def, DepthSepConv):
                    end_point = end_point_base + '_depthwise'

                    # By passing filters=None
                    # separable_conv2d produces only a depthwise convolution layer
                    net = slim.separable_conv2d(net, None, conv_def.kernel,
                                                depth_multiplier=1,
                                                stride=layer_stride,
                                                rate=layer_rate,
                                                normalizer_fn=slim.batch_norm,
                                                scope=end_point)

                    end_points[end_point] = net
                    if end_point == final_endpoint:
                        return net, end_points

                    end_point = end_point_base + '_pointwise'

                    net = slim.conv2d(net, depth(conv_def.depth), [1, 1],
                                      stride=1,
                                      normalizer_fn=slim.batch_norm,
                                      scope=end_point)

                    end_points[end_point] = net
                    if end_point == final_endpoint:
                        return net, end_points
                else:
                    raise ValueError('Unknown convolution type %s for layer %d'
                                     % (conv_def.ltype, i))
    raise ValueError('Unknown final endpoint %s' % final_endpoint)


def mobilenet_v1(inputs,
                 num_classes=1000,
                 dropout_keep_prob=0.999,
                 is_training=True,
                 min_depth=8,
                 depth_multiplier=1.0,
                 conv_defs=None,
                 prediction_fn=tf.contrib.layers.softmax,
                 spatial_squeeze=True,
                 reuse=None,
                 scope='MobilenetV1'):
    """Mobilenet v1 model for classification.

    Args:
    inputs: a tensor of shape [batch_size, height, width, channels].
    num_classes: number of predicted classes.
    dropout_keep_prob: the percentage of activation values that are retained.
    is_training: whether is training or not.
    min_depth: Minimum depth value (number of channels) for all convolution ops.
      Enforced when depth_multiplier < 1, and not an active constraint when
      depth_multiplier >= 1.
    depth_multiplier: Float multiplier for the depth (number of channels)
      for all convolution ops. The value must be greater than zero. Typical
      usage will be to set this value in (0, 1) to reduce the number of
      parameters or computation cost of the model.
    conv_defs: A list of ConvDef namedtuples specifying the net architecture.
    prediction_fn: a function to get predictions out of logits.
    spatial_squeeze: if True, logits is of shape is [B, C], if false logits is
        of shape [B, 1, 1, C], where B is batch_size and C is number of classes.
    reuse: whether or not the network and its variables should be reused. To be
      able to reuse 'scope' must be given.
    scope: Optional variable_scope.

    Returns:
    logits: the pre-softmax activations, a tensor of size
      [batch_size, num_classes]
    end_points: a dictionary from components of the network to the corresponding
      activation.

    Raises:
    ValueError: Input rank is invalid.
    """
    input_shape = inputs.get_shape().as_list()
    if len(input_shape) != 4:
        raise ValueError('Invalid input tensor rank, expected 4, was: %d' %
                         len(input_shape))

    with tf.variable_scope(scope, 'MobilenetV1', [inputs, num_classes],
                           reuse=reuse) as scope:
        with slim.arg_scope([slim.batch_norm, slim.dropout],
                            is_training=is_training):
            net, end_points = mobilenet_v1_base(inputs, scope=scope,
                                                min_depth=min_depth,
                                                depth_multiplier=depth_multiplier,
                                                conv_defs=conv_defs)
            with tf.variable_scope('Logits'):
                kernel_size = _reduced_kernel_size_for_small_input(net, [7, 7])
                net = slim.avg_pool2d(net, kernel_size, padding='VALID',
                                      scope='AvgPool_1a')
                end_points['AvgPool_1a'] = net
                # 1 x 1 x 1024
                net = slim.dropout(net, keep_prob=dropout_keep_prob, scope='Dropout_1b')
                logits = slim.conv2d(net, num_classes, [1, 1], activation_fn=None,
                                     normalizer_fn=None, scope='Conv2d_1c_1x1')
                if spatial_squeeze:
                    logits = tf.squeeze(logits, [1, 2], name='SpatialSqueeze')
            end_points['Logits'] = logits
            if prediction_fn:
                end_points['Predictions'] = prediction_fn(logits, scope='Predictions')
    return logits, end_points

mobilenet_v1.default_image_size = 224


def wrapped_partial(func, *args, **kwargs):
    partial_func = functools.partial(func, *args, **kwargs)
    functools.update_wrapper(partial_func, func)
    return partial_func


mobilenet_v1_075 = wrapped_partial(mobilenet_v1, depth_multiplier=0.75)
mobilenet_v1_050 = wrapped_partial(mobilenet_v1, depth_multiplier=0.50)
mobilenet_v1_025 = wrapped_partial(mobilenet_v1, depth_multiplier=0.25)


def _reduced_kernel_size_for_small_input(input_tensor, kernel_size):
    """Define kernel size which is automatically reduced for small input.

    If the shape of the input images is unknown at graph construction time this
    function assumes that the input images are large enough.

    Args:
    input_tensor: input tensor of size [batch_size, height, width, channels].
    kernel_size: desired kernel size of length 2: [kernel_height, kernel_width]

    Returns:
    a tensor with the kernel size.
    """
    shape = input_tensor.get_shape().as_list()
    if shape[1] is None or shape[2] is None:
        kernel_size_out = kernel_size
    else:
        kernel_size_out = [min(shape[1], kernel_size[0]),
                           min(shape[2], kernel_size[1])]
    return kernel_size_out


def mobilenet_v1_arg_scope(is_training=True,
                           weight_decay=0.00004,
                           stddev=0.09,
                           regularize_depthwise=False):
    """Defines the default MobilenetV1 arg scope.

    Args:
    is_training: Whether or not we're training the model.
    weight_decay: The weight decay to use for regularizing the model.
    stddev: The standard deviation of the trunctated normal weight initializer.
    regularize_depthwise: Whether or not apply regularization on depthwise.

    Returns:
    An `arg_scope` to use for the mobilenet v1 model.
    """
    batch_norm_params = {
        'is_training': is_training,
        'center': True,
        'scale': True,
        'decay': 0.9997,
        'epsilon': 0.001,
    }

    # Set weight_decay for weights in Conv and DepthSepConv layers.
    weights_init = tf.truncated_normal_initializer(stddev=stddev)
    regularizer = tf.contrib.layers.l2_regularizer(weight_decay)
    if regularize_depthwise:
        depthwise_regularizer = regularizer
    else:
        depthwise_regularizer = None
    with slim.arg_scope([slim.conv2d, slim.separable_conv2d],
                        weights_initializer=weights_init,
                        activation_fn=tf.nn.relu6, normalizer_fn=slim.batch_norm):
        with slim.arg_scope([slim.batch_norm], **batch_norm_params):
            with slim.arg_scope([slim.conv2d], weights_regularizer=regularizer):
                with slim.arg_scope([slim.separable_conv2d],
                                weights_regularizer=depthwise_regularizer) as sc:
                    return sc


# ---------------------------------------------------------------------------------------------------------------------
# Added in this repo

logger = get_logger(name=__name__, level='debug')


class MobileNetDefaultFile(object):
    MODEL_REPO_BASE_URL = 'http://download.tensorflow.org/models/'
    MODEL_DATE = '2017_06_14'
    MODEL_BASE_FMT = 'mobilenet_v1_{}_{}'
    MODEL_DL_FMT = MODEL_BASE_FMT + '_{}.tar.gz'
    MODEL_PB_FMT = MODEL_BASE_FMT + '.pb'
    MODEL_FACTOR = '0.50'
    IMG_SIZE = 224


class MobileNetV1Restored(object):
    def __init__(self, img_size=224, model_factor=1.0, weight_decay=0.0, num_classes=1001,
                 input_node_name='input', output_node_name='output',
                 logs_directory='/tmp/tf-logs/'):
        self.img_size = img_size
        self.model_factor = model_factor
        self.weight_decay = weight_decay
        self.num_classes = num_classes

        # Store node names for useful tensors
        self.input_node_name = input_node_name
        self.output_node_name = output_node_name

        self.input_tensor = None
        self.output_tensor = None
        self.embedding_tensor = None

        self.labels = load_imagenet_labels()

        self.logs_directory = logs_directory

        if not os.path.exists(self.logs_directory):
            os.mkdir(self.logs_directory)

        # Start an interactive session
        self.sess = tf.InteractiveSession()

    @staticmethod
    def load_frozen_graph(pb_file, graph_name='mobilenet'):
        graph = tf.Graph()
        graph_def = tf.GraphDef()

        with open(pb_file, "rb") as f:
            graph_def.ParseFromString(f.read())
        with graph.as_default():
            tf.import_graph_def(
                graph_def,
                input_map=None,
                return_elements=None,
                name=graph_name,
                op_dict=None,
                producer_op_list=None
            )

        return graph

    def restore_session_from_checkpoint(self, filename, tensorboard=True):
        # tf.reset_default_graph()

        # Insert Input placeholder for images
        self.input_tensor = tf.placeholder(tf.float32, shape=(None, self.img_size, self.img_size, 3),
                                           name=self.input_node_name)
        arg_scope = mobilenet_v1_arg_scope(weight_decay=self.weight_decay)
        with slim.arg_scope(arg_scope):
            logits, end_points = mobilenet_v1(self.input_tensor, num_classes=self.num_classes,
                                              is_training=False,
                                              depth_multiplier=self.model_factor)

        predictions = tf.contrib.layers.softmax(logits)
        self.output_tensor = tf.identity(predictions, name=self.output_node_name)

        self.embedding_tensor = end_points['AvgPool_1a']

        # We retrieve the protobuf graph definition
        graph = tf.get_default_graph()

        # Add ops to restore all the variables
        rest_var = slim.get_variables_to_restore()  # TODO: change this! maybe it can optimize the final network

        saver = tf.train.Saver(rest_var)
        saver.restore(self.sess, filename)

        if tensorboard:
            tf.summary.FileWriter(self.logs_directory, graph=graph)

        return graph

    def restore_session_from_frozen_graph(self, filename, tensorboard=True):
        graph = self.load_frozen_graph(filename, graph_name='mobilenet')

        self.sess = tf.InteractiveSession(graph=graph)

        self.input_tensor = graph.get_tensor_by_name('mobilenet/'+self.input_node_name+':0')
        self.output_tensor = graph.get_tensor_by_name('mobilenet/'+self.output_node_name+':0')
        self.embedding_tensor = graph.get_tensor_by_name('mobilenet/MobilenetV1/Logits/AvgPool_1a/AvgPool:0')

        if tensorboard:
            tf.summary.FileWriter(self.logs_directory, graph=graph)

        return graph

    def freeze_inference_graph(self, input_checkpoint, output_filename='frozen_graph.pb'):
        graph = self.restore_session_from_checkpoint(input_checkpoint)
        input_graph_def = graph.as_graph_def()

        # We retrieve our checkpoint fullpath
        basedir = os.path.dirname(input_checkpoint)
        output_filename = os.path.join(basedir, output_filename)

        # We use a built-in TF helper to export variables to constants
        output_graph_def = graph_util.convert_variables_to_constants(
            self.sess,  # The session is used to retrieve the weights
            input_graph_def,  # The graph_def is used to retrieve the nodes
            self.output_node_name.split(",")  # The output node names are used to select the useful nodes
        )

        # Finally we serialize and dump the output graph to the filesystem
        with tf.gfile.GFile(output_filename, "wb") as f:
            f.write(output_graph_def.SerializeToString())
        logger.info("%i ops in the final graph.", len(output_graph_def.node))

    def get_output(self, nparr, get_embedding=False):
        if self.sess is None:
            raise ValueError("TensorFlow session was not initialized! "
                             "Restore a session before predicting.")

        if get_embedding:
            prediction, embedding = self.sess.run((self.output_tensor, self.embedding_tensor),
                                                  {self.input_tensor: nparr})
            prediction = np.squeeze(prediction)
            embedding = np.squeeze(embedding)
            output = prediction, embedding
        else:
            prediction = self.sess.run(self.output_tensor, {self.input_tensor: nparr})
            prediction = np.squeeze(prediction)
            output = prediction
        return output

    def predict_on_images(self, images_path):

        # Now load model and make inferences
        predictions = []

        t_ini = time.time()

        for fn in os.listdir(images_path):
            if not fn.endswith('.jpg') and not fn.endswith('.png'):
                continue

            logger.info("Processing image '%s' and making prediction...", fn)
            img = self.load_and_prepare_image(os.path.join(images_path, fn), img_size=self.img_size)

            tic = time.time()
            prediction = self.get_output(img, get_embedding=False)
            toc = time.time()

            logger.info("Prediction made in %.4f sec", toc-tic)

            predictions.append((fn, prediction))

        t_end = time.time()

        logger.info("Elapsed time on making %i predictions: %.4f sec",
                    len(predictions), t_end - t_ini)

        return dict(predictions)

    def prediction_to_classes(self, prediction, n_top=10):
        top_predictions = sorted(enumerate(prediction), key=lambda i_p: -i_p[1])[:n_top]
        return [(self.labels[i], p) for (i, p) in top_predictions]

    def convert_tflite_format(self, output_filename, quantized=False):
        inference_type = QUANTIZED_UINT8 if quantized else FLOAT
        quantized_input_stats = None if QUANTIZED_UINT8 else None  # TODO: fill this!

        success = toco_convert(input_data=self.sess.graph_def, input_tensors=[self.input_tensor],
                               output_tensors=[self.output_tensor, self.embedding_tensor],
                               inference_type=inference_type, quantized_input_stats=quantized_input_stats,
                               output_filename=output_filename)

        return success

    @staticmethod
    def load_and_prepare_image(filename, img_size=224):
        """

        :param filename:
        :param img_size:
        :return:
        """
        img = imread(filename, flatten=False)
        img = imresize(img, (img_size, img_size))
        img = img.astype(np.float32)
        img = np.expand_dims(img, 0)

        # Preprocess
        img = (img - 127.) / 127.

        return img

    @staticmethod
    def read_tensor_from_image_file(file_name, input_height=224, input_width=224, input_mean=-127, input_std=127):
        input_name = "file_reader"
        output_name = "normalized"
        file_reader = tf.read_file(file_name, input_name)

        if file_name.endswith(".png"):
            image_reader = tf.image.decode_png(file_reader, channels=3, name='png_reader')
        elif file_name.endswith(".gif"):
            image_reader = tf.squeeze(tf.image.decode_gif(file_reader, name='gif_reader'))
        elif file_name.endswith(".bmp"):
            image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
        else:
            image_reader = tf.image.decode_jpeg(file_reader, channels=3, name='jpeg_reader')

        float_caster = tf.cast(image_reader, tf.float32)
        dims_expander = tf.expand_dims(float_caster, 0)
        resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
        normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
        sess = tf.Session()
        result = sess.run(normalized)

        return result

