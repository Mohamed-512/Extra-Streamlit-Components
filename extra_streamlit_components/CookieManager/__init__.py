import os

import streamlit.components.v1 as components
import datetime

from extra_streamlit_components import IS_RELEASE

if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("cookie_manager", path=build_path)
else:
    _component_func = components.declare_component("cookie_manager", url="http://localhost:3001")


class CookieManager:
    def __init__(self, key="init"):
        self.cookie_manager = _component_func
        self.cookies = self.cookie_manager(method="getAll", key=key, default={})

    def get(self, cookie: str):
        return self.cookies.get(cookie)

    def set(self, cookie, val, expires_at=None, key="set"):
        if cookie is None or cookie == "":
            return

        if expires_at is None:
            expires_at = datetime.datetime.now() + datetime.timedelta(days=1)

        expires_at = expires_at.isoformat()
        did_add = self.cookie_manager(method="set", cookie=cookie, value=val,
                                      expires_at=expires_at, key=key, default=False)
        if did_add:
            self.cookies[cookie] = val

    def delete(self, cookie, key="delete"):
        if cookie is None or cookie == "":
            return
        did_add = self.cookie_manager(method="delete", cookie=cookie, key=key, default=False)
        if did_add:
            del self.cookies[cookie]

    def get_all(self, key="get_all"):
        self.cookies = self.cookie_manager(method="getAll", key=key, default={})
        return self.cookies
