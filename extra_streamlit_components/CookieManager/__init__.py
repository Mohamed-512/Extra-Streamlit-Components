import os
import streamlit.components.v1 as components
import streamlit as st
import uuid

from extra_streamlit_components import IS_RELEASE

if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("cookie_manager", path=build_path)
else:
    _component_func = components.declare_component("cookie_manager", url="http://localhost:3001")


class CookieManager:
    def __init__(self):
        self.cookie_manager = _component_func
        self.cookies = self.cookie_manager(method="getAll", key="AA")

        self.use_streamlit_state = False
        if st is not None and int(str(st.__version__).split(".")[1]) >= 84:
            self.use_streamlit_state = True
            if 'cookies' not in st.session_state.keys() or st.session_state.cookies == {}:
                st.session_state['cookies'] = self.cookies
            elif st.session_state.cookies is None:
                st.session_state['cookies'] = {}

    def get(self, cookie: str, key: any = 0) -> any:
        try:
            if self.use_streamlit_state and "cookies" in st.session_state and st.session_state.cookies is not None:
                return st.session_state.cookies.get(cookie)
            return self.cookies.get(cookie)
        except:
            return None
    def set(self, cookie, val, key: any = 0):
        if cookie is None or cookie == "":
            return

        self.cookie_manager(method="set", cookie=cookie, value=val, key=f"1{key}")

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
        if self.use_streamlit_state:
            data = st.session_state.cookies
        else:
            data = self.cookies
        if data is None or data == {}:
            self.cookies = self.cookie_manager(method="getAll", key=str(uuid.uuid4()))
            return self.cookies
        return data
