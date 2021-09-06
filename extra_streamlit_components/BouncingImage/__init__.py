import os
import streamlit.components.v1 as components
from streamlit.components.v1.components import CustomComponent

from extra_streamlit_components import IS_RELEASE

if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("bouncing_image", path=build_path)
else:
    _component_func = components.declare_component("bouncing_image", url="http://localhost:3001")


def bouncing_image(image_source: str, animate: bool, animation_time: int, height: float, width: float) -> CustomComponent:
    component_value = _component_func(image=image_source, animate=animate, animation_time=animation_time, height=height, width=width)
    if component_value is None:
        return False
    return component_value
