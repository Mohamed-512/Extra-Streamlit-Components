import streamlit as st
import Components as stx

st.set_page_config(layout="centered")

# chosen_id = stx.tab_bar(data=[
#     stx.TabBarItemData(id=1, title="ToDo", description="Tasks to take care of"),
#     stx.TabBarItemData(id=2, title="Done", description="Tasks taken care of"),
# ])
#
# st.write(f"{chosen_id=}")

image_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg"
# image_url = "https://en.logodownload.org/wp-content/uploads/2020/02/Iberdrola-logo-11.png"

animating = stx.bouncing_image(image_source=image_url, animate=st.checkbox("Animate"), animation_time=3750, height=100, width=320)
st.write(f"{animating=}")
