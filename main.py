import streamlit as st
import extra_streamlit_components as stx
import datetime


def show_router_controls():
    @st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
    def init_router():
        return stx.Router({"/home": home, "/landing": landing})

    def home():
        return st.write("This is a home page")

    def landing():
        return st.write("This is the landing page")

    router = init_router()
    router.show_route_view()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.header("Current route")
        current_route = router.get_url_route()
        st.write(f"{current_route}")
    with c2:
        st.header("Set route")
        new_route = st.text_input("route")
        if st.button("Route now!"):
            router.route(new_route)
    with c3:
        st.header("Session state")
        st.write(st.session_state)


def show_cookie_manager_controls():
    st.write("# Cookie Manager")

    @st.cache(allow_output_mutation=True)
    def get_manager():
        return stx.CookieManager()

    cookie_manager = get_manager()

    st.subheader("All Cookies:")
    cookies = cookie_manager.get_all()
    st.write(cookies)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("Get Cookie:")
        cookie = st.text_input("Cookie", key="0")
        clicked = st.button("Get")
        if clicked:
            value = cookie_manager.get(cookie=cookie)
            st.write(value)
    with c2:
        st.subheader("Set Cookie:")
        cookie = st.text_input("Cookie", key="1")
        val = st.text_input("Value")
        if st.button("Add"):
            cookie_manager.set(cookie, val, expires_at=datetime.datetime(year=2022, month=2, day=2))
    with c3:
        st.subheader("Delete Cookie:")
        cookie = st.text_input("Cookie", key="2")
        if st.button("Delete"):
            cookie_manager.delete(cookie)


def show_bouncing_image():
    st.write("# Bouncing Image")

    image_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg"
    stx.bouncing_image(image_source=image_url, animate=True,
                       animation_time=2000, height=145, width=500)

    st.code("""
    image_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg"
    stx.bouncing_image(image_source=image_url, animate=True, animation_time=2000, height=145, width=500)
    """)


def show_top_bar():
    st.write("# Tab Bar")

    chosen_id = stx.tab_bar(data=[
        stx.TabBarItemData(id=1, title="ToDo",
                           description="Tasks to take care of"),
        stx.TabBarItemData(id=2, title="Done",
                           description="Tasks taken care of"),
        stx.TabBarItemData(id=3, title="Overdue",
                           description="Tasks missed out"),
    ], default=1, return_type=int)

    st.info(f"chosen_id = {chosen_id}, type = {type(chosen_id)}")

    st.code("""
    chosen_id = stx.tab_bar(data=[
        stx.TabBarItemData(id=1, title="ToDo", description="Tasks to take care of"),
        stx.TabBarItemData(id=2, title="Done", description="Tasks taken care of"),
        stx.TabBarItemData(id=3, title="Overdue", description="Tasks missed out"),
    ], default=1)
    """)


def show_stepper_bar():
    st.write("# Stepper Bar")
    c1, c2, c3 = st.columns([1, 3, 1])
    with c1:
        st.write("Horizontal")
    with c2:
        is_vertical = (st.slider("Orientation", min_value=0, max_value=1, value=0) or 0) == 1
    with c3:
        st.write("Vertical")

    is_sequence_locked = st.checkbox("Lock Sequence", value=True)

    if is_vertical:
        c1, c2 = st.columns([1, 3])
        with c1:
            val = stx.stepper_bar(steps=["Ready", "Get Set", "Go"], is_vertical=is_vertical, lock_sequence=is_sequence_locked)
        with c2:
            st.info(f"Phase #{val}")
    else:
        val = stx.stepper_bar(steps=["Ready", "Get Set", "Go"], is_vertical=is_vertical, lock_sequence=is_sequence_locked)

        st.info(f"Phase #{val}")

    st.code("""
        val = stx.stepper_bar(steps=["Ready", "Get Set", "Go"], is_vertical=False)
    """)


if __name__ == "__main__":
    show_router_controls()
    st.write("_______")
    show_cookie_manager_controls()
    st.write("_______")
    show_top_bar()
    st.write("_______")
    show_bouncing_image()
    st.write("_______")
    show_stepper_bar()
