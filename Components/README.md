# Extra Streamlit Components

An all-in-one place, to find complex or just not available components by default on streamlit.

## Components

- ### TabBar
  Inspire from React's `ScrollMenu`, this component receives a list of `TabBarItemData`, and returns the `id` of the
  selected tab

  ***Inputs***:
    - data: List[TabBarItemData]
    - default=None _(optional)_

  ***Returns***:
    - id: int


- ### BouncingImage
  Probably not the best naming but this component, renders an image by its path or url, and animates by zooming in and
  out repetitively giving an illusion of a bounce.

  ***Inputs***:
    - image_source: str
    - animate: bool
    - animation_time: int
    - height: float
    - width: float

  ***Returns***:
    - is_animating: bool
