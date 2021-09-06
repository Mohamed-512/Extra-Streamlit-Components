import os
import streamlit.components.v1 as components
from streamlit.components.v1.components import CustomComponent
from typing import List

from extra_streamlit_components import IS_RELEASE

if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("stepper_bar", path=build_path)
else:
    _component_func = components.declare_component("stepper_bar", url="http://localhost:3001")


def stepper_bar(steps: List[str]) -> CustomComponent:
    component_value = _component_func(steps=steps, default=0)
    if component_value is None:
        return 0
    return component_value
