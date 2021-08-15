# Extra-Streamlit-Components

[![Downloads](https://pepy.tech/badge/extra-streamlit-components)](https://pepy.tech/project/extra-streamlit-components)

An all-in-one place, to find complex or just not available components by default on streamlit.

## Components

Firstly, add `import extra_streamlit_components as stx`

- ### Cookie Manager
  The long awaited between-sessions in-browser cookies store and manager! It stores cookies in a strict same-site behaviour. 
  
  **P.S.** For best experience use _streamlit>=0.84.0_
  ```python
  cookie_manager = stx.CookieManager()

  st.subheader("All Cookies:")
  cookies = cookie_manager.get_all()
  st.write(cookies)
 
  c1, c2, c3 = st.beta_columns(3)
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
  ```

  ![](Demo_Assets/cookie_manager.gif)

- ### TabBar
  Inspire from React's `ScrollMenu`, this component receives a list of `TabBarItemData`, and returns the `id` of the
  selected tab
  ```python
  chosen_id = stx.tab_bar(data=[
      stx.TabBarItemData(id=1, title="ToDo", description="Tasks to take care of"),
      stx.TabBarItemData(id=2, title="Done", description="Tasks taken care of"),
      stx.TabBarItemData(id=3, title="Overdue", description="Tasks missed out"),
  ], default=1)
  st.info(f"{chosen_id=}")
  ```

  ![](Demo_Assets/tab_bar.gif)


- ### BouncingImage
  Probably not the best naming but this component, renders an image by its path or url, and animates by zooming in and
  out repetitively giving an illusion of a bounce.

  ```python
  image_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg"
  stx.bouncing_image(image_source=image_url, animate=True, animation_time=1500, height=200, width=600)
  ```
  ![](Demo_Assets/bouncing_images.gif)

- ### StepperBar
  A streamlit wrapper on MaterialUI's Stepper

  ```python
  val = stx.stepper_bar(steps=["Ready", "Get Set", "Go"])
  st.info(f"Phase #{val}")
  ```
  ![](Demo_Assets/stepper_bar_demo.gif)
