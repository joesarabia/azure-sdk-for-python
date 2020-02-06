# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StreamingEntityScaleUnit(Model):
    """scale units definition.

    :param scale_unit: The scale unit number of the StreamingEndpoint.
    :type scale_unit: int
    """

    _attribute_map = {
        'scale_unit': {'key': 'scaleUnit', 'type': 'int'},
    }

    def __init__(self, *, scale_unit: int=None, **kwargs) -> None:
        super(StreamingEntityScaleUnit, self).__init__(**kwargs)
        self.scale_unit = scale_unit