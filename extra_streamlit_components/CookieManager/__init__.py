import os
import streamlit.components.v1 as components
import streamlit as st
import uuid
import datetime

from extra_streamlit_components import IS_RELEASE

if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component(
        "cookie_manager", path=build_path)
else:
    _component_func = components.declare_component(
        "cookie_manager", url="http://localhost:3001")


def compare_versions(v1: str, v2: str):
    v1 = v1.split(".")
    v2 = v2.split(".")

    if len(v1) != len(v2):
        return len(v1) > len(v2)

    for i in range(len(v1)):
        if int(v1[i]) != int(v2[i]):
            return int(v1[i]) > int(v2[i])

    return False


class CookieManager:
    def __init__(self):
        self.cookie_manager = _component_func
        self.use_streamlit_state = False

        if st is not None and compare_versions(st.__version__, "0.84.1"):
            self.use_streamlit_state = True
            if 'cookies' not in st.session_state or ('cookies' in st.session_state and st.session_state.cookies is None):
                st.session_state['cookies'] = self.cookie_manager(
                    method="getAll", key="cookie_manager")

    def get(self, cookie: str, key: any = 0) -> any:
        try:
            if self.use_streamlit_state and "cookies" in st.session_state and st.session_state.cookies is not None:
                return st.session_state.cookies.get(cookie)
            return self.cookies.get(cookie)
        except:
            c = self.get_all()
            if c is not None:
                c.get(cookie)
            return None

    def set(self, cookie, val, expires_at=datetime.datetime.now() + datetime.timedelta(days=1), key: any = 0):
        if cookie is None or cookie == "":
            return
        expires_at = expires_at.isoformat()
        self.cookie_manager(method="set", cookie=cookie,
                            value=val, expires_at=expires_at, key=f"1{key}")

        if self.use_streamlit_state:
            st.session_state.cookies.update({cookie: val})
        else:
            self.cookies.update({cookie: val})

    def delete(self, cookie, key: any = 0):
        if cookie is None or cookie == "":
            return
        self.cookie_manager(method="delete", cookie=cookie, key=f"2{key}")

        if self.use_streamlit_state and cookie in st.session_state.cookies:
            st.session_state.cookies.pop(cookie)
        elif cookie in self.cookies:
            self.cookies.pop(cookie)

    def get_all(self, key: any = 0) -> dict:
        data = None
        if self.use_streamlit_state:
            data = st.session_state.cookies
        elif data is None or data == {}:
            self.cookies = self.cookie_manager(
                method="getAll", key="str(uuid.uuid4())")
            return self.cookies
        return data
