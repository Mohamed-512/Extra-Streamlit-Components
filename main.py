import streamlit as st
import extra_streamlit_components as stx


def show_cookie_manager_controls():
    st.write("# Cookie Manager")

    cookie_manager = stx.CookieManager()

    st.subheader("All Cookies:")

    cookies = cookie_manager.get_all()
    st.write(cookies)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("Get Cookie:")
        cookie = st.text_input("Cookie", key="0")

        clicked = st.button("Get")

        if clicked:
            value = cookie_manager.get(cookie)
            st.write(value)
    with c2:
        st.subheader("Set Cookie:")
        cookie = st.text_input("Cookie", key="1")
        val = st.text_input("Value")

        if st.button("Add"):
            cookie_manager.set(cookie, val)

    with c3:
        st.subheader("Delete Cookie:")
        cookie = st.text_input("Cookie", key="2")

        if st.button("Delete"):
            cookie_manager.delete(cookie)


def show_bouncing_image():
    st.write("# Bouncing Image")

    image_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg"
    stx.bouncing_image(image_source=image_url, animate=True, animation_time=2000, height=145, width=500)

    st.code("""
    image_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg"
    stx.bouncing_image(image_source=image_url, animate=True, animation_time=2000, height=145, width=500)
    """)


def show_top_bar():
    st.write("# Top Bar")

    chosen_id = stx.tab_bar(data=[
        stx.TabBarItemData(id=1, title="ToDo", description="Tasks to take care of"),
        stx.TabBarItemData(id=2, title="Done", description="Tasks taken care of"),
        stx.TabBarItemData(id=3, title="Overdue", description="Tasks missed out"),
    ], default=1)

    st.info(f"chosen_id = {chosen_id}")

    st.code("""
    chosen_id = stx.tab_bar(data=[
        stx.TabBarItemData(id=1, title="ToDo", description="Tasks to take care of"),
        stx.TabBarItemData(id=2, title="Done", description="Tasks taken care of"),
        stx.TabBarItemData(id=3, title="Overdue", description="Tasks missed out"),
    ], default=1)
    """)


def show_stepper_bar():
    st.write("# Stepper Bar")

    val = stx.stepper_bar(steps=["Ready", "Get Set", "Go"])
    st.info(f"Phase #{val}")

    st.code("""
        val = stx.stepper_bar(steps=["Ready", "Get Set", "Go"])
    """)


show_cookie_manager_controls()
st.write("_______")
show_top_bar()
st.write("_______")
show_bouncing_image()
st.write("_______")
show_stepper_bar()
