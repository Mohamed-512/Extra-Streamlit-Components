import time

import streamlit as st
import extra_streamlit_components as stx

st.set_page_config(layout="wide")


def show_splash():
    image_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg"

    if st.experimental_get_query_params().get("t") is None:
        st.experimental_set_query_params(t=int(time.time()))

    return stx.bouncing_image(image_source=image_url, animate=True, animation_time=2000, height=145, width=320)


def show_data():
    chosen_id = stx.tab_bar(data=[
        stx.TabBarItemData(id=1, title="ToDo", description="Tasks to take care of"),
        stx.TabBarItemData(id=2, title="Done", description="Tasks taken care of"),
        stx.TabBarItemData(id=3, title="Overdue", description="Tasks missed out"),
    ])

    st.info(f"{chosen_id=}")

    st.write("______________________")

    """
# Lorem ipsum

dolor sit amet, consectetur adipiscing elit. Nulla porttitor laoreet sagittis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ligula lacus, vulputate eget ultricies vitae, iaculis sed eros. Nunc eu consequat libero, id lacinia libero. Suspendisse tincidunt magna quis orci maximus dapibus. Pellentesque mollis leo eu eros ultrices gravida. Mauris sit amet ex vel tortor aliquam imperdiet ut consequat neque.
Phasellus aliquet feugiat tempus. Sed mattis porta orci ac laoreet. Donec ut massa et nisl commodo hendrerit. Nullam porta tortor quis metus scelerisque dapibus. Donec aliquet ex nec libero dapibus accumsan. Aenean semper vestibulum erat, tincidunt iaculis ipsum fringilla at. In diam ex, fermentum gravida sagittis in, euismod vel quam.
Aliquam aliquam ac orci quis scelerisque. Suspendisse potenti. Vestibulum suscipit pharetra elit, sed lacinia ex efficitur et. Duis sagittis sapien at tincidunt ultrices. Cras pulvinar velit quam, id fermentum metus aliquet at. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum nec ultricies orci, lobortis dictum orci. Etiam tempus cursus blandit. Nam ultrices eu tortor id dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus non elementum purus. Vestibulum ullamcorper justo nibh, sed egestas quam suscipit a. In id orci nulla. Donec vehicula laoreet libero vitae congue. Vestibulum vel nibh orci. Curabitur eu erat sed justo ullamcorper porta. Curabitur gravida, ipsum ac hendrerit molestie, diam mi facilisis massa, vitae malesuada arcu orci at magna. Aliquam ornare leo sit amet dictum tristique. Integer iaculis metus a accumsan accumsan. Etiam id tristique nibh, consectetur blandit elit.
Donec ut leo sed mauris bibendum laoreet sed ac odio. Suspendisse potenti. Vestibulum urna arcu, consequat quis laoreet vitae, pharetra in ligula. Nulla gravida rutrum massa vitae auctor. Vivamus blandit placerat orci. Morbi blandit cursus nibh, at venenatis lorem hendrerit sed. Sed vel est in lectus fermentum suscipit sed at urna.
    """


open_time = st.experimental_get_query_params().get("t")

is_loaded = False

if type(open_time) is list:
    is_loaded = time.time() > int(open_time[0]) + 4

if is_loaded:
    show_data()
else:
    show_splash()
