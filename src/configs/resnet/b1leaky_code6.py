import torch.nn as nn

RES_INPUT = (128, 64, 64)
RES_OUTPUT = RES_INPUT

IMAGE_DIMENSIONS = (1, 256, 256)
t_bias = True

g_structure = {
    'type': 'resnet_translator',
    'encode_stack': {
        'input': IMAGE_DIMENSIONS,
        'output': RES_INPUT,
        'filters': [
            {
                'type': 'normal',
                'out_channels': 32,
                'kernel_size': 9,
                'stride': 1,
                'padding': 4,
                'bias': False,
                'pre_batch_norm': nn.BatchNorm2d(32),
                'activation': nn.ReLU(True),
                'post_batch_norm': False
            },
            {
                'type': 'normal',
                'out_channels': 64,
                'kernel_size': 6,
                'stride': 2,
                'padding': 2,
                'bias': t_bias,
                'pre_batch_norm': nn.BatchNorm2d(64),
                'activation': nn.ReLU(True),
                'post_batch_norm': False
            },
            {
                'type': 'normal',
                'out_channels': 128,
                'kernel_size': 6,
                'stride': 2,
                'padding': 2,
                'bias': t_bias,
                'pre_batch_norm': nn.BatchNorm2d(128),
                'activation': nn.ReLU(True),
                'post_batch_norm': False
            },
        ]

    },
    'res_blocks': {
        'n_blocks': 1,
        'input_shape': RES_INPUT,
        'kernel_size': (3,3)
    },
    'decode_stack': {
        'input': RES_OUTPUT,
        'output': IMAGE_DIMENSIONS,
        'filters': [
            {
                'type': 'transpose',
                'out_channels': 64,
                'kernel_size': 6,
                'stride': 2,
                'padding': 2,
                'output_padding': 0,
                'bias': t_bias,
                'pre_batch_norm': nn.BatchNorm2d(64),
                'activation': nn.LeakyReLU(inplace=True),
                'post_batch_norm': False
            },
            {
                'type': 'transpose',
                'out_channels': 32,
                'kernel_size': 6,
                'stride': 2,
                'padding': 2,
                'output_padding': 0,
                'bias': t_bias,
                'pre_batch_norm': nn.BatchNorm2d(32),
                'activation': nn.LeakyReLU(inplace=True),
                'post_batch_norm': False
            },
            {
                'type': 'normal',
                'out_channels': IMAGE_DIMENSIONS[0],
                'kernel_size': 9,
                'stride': 1,
                'padding': 4,
                'bias': True,
                'pre_batch_norm': None,
                'activation': nn.Tanh(),
                'post_batch_norm': False
            },
        ]

    }

}
