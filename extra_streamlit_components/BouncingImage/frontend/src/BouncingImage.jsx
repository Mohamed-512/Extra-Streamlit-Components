import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React from "react"

import { withStyles, createStyles } from "@material-ui/core/styles"
import Grow from "@material-ui/core/Grow"
import CardMedia from "@material-ui/core/CardMedia"

const styles = createStyles((theme) => ({
  root: {
    height: 180,
  },
  container: {
    display: "flex",
  },
  paper: {
    margin: 1,
  },
  svg: {
    width: 100,
    height: 100,
  },
  polygon: {
    fill: "white",
    stroke: "red",
    strokeWidth: 1,
  },
}))

class BouncingImage extends StreamlitComponentBase {
  state = {
    animationTimeRoundTrip: 1750,
    isAnimating: true,
    keepAnimating: false,
  }

  constructor(props) {
    super(props)
  }

  componentDidMount() {
    const { animation_time, animate } = this.props.args

    Streamlit.setComponentValue(animate)
    this.setState(
      () => ({
        animationTimeRoundTrip: animation_time,
        keepAnimating: animate,
      }),
      () =>
        setInterval(
          () =>
            this.state.keepAnimating &&
            this.setState(
              () => ({
                isAnimating:
                  !this.state.isAnimating && this.state.keepAnimating,
              }),
              () => Streamlit.setComponentValue(this.state.keepAnimating)
            ),
          this.state.animationTimeRoundTrip / 2
        )
    )
  }

  render = () => {
    const isAnimating = this.state.isAnimating
    let {
      classes,
      args: { image, height, width },
    } = this.props

    return (
      <div className={classes.root}>
        <div className={classes.container}>
          <Grow
            in={isAnimating}
            style={{ transformOrigin: "0 0 0" }}
            {...(isAnimating
              ? { timeout: this.state.animationTimeRoundTrip / 2 }
              : {})}
          >
            <CardMedia image={image} style={{ height, width }} />
          </Grow>
        </div>
      </div>
    )
  }
}

export default withStreamlitConnection(withStyles(styles)(BouncingImage))
