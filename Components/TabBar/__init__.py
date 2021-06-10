import os
import streamlit.components.v1 as components
from dataclasses import dataclass
from typing import List
from Components import IS_RELEASE

if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("tab_bar", path=build_path)
else:
    _component_func = components.declare_component("tab_bar", url="http://localhost:3001")


@dataclass(frozen=True, order=True, unsafe_hash=True)
class TabBarItemData:
    id: int
    title: str
    description: str

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}


def tab_bar(data: List[TabBarItemData], default=None, key=None):
    data = list(map(lambda item: item.to_dict(), data))
    component_value = _component_func(data=data, selectedId=default, key=key, default=default)

    return component_value
