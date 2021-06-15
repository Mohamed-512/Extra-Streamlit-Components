import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React from "react"

import { withStyles, createStyles } from "@material-ui/core/styles"
import Stepper from "@material-ui/core/Stepper"
import Step from "@material-ui/core/Step"
import StepLabel from "@material-ui/core/StepLabel"

const styles = createStyles((theme) => ({
  root: {
    width: "100%",
    backgroundColor: "transparent",
  },
  icon: {
    color: "grey",
    cursor: "pointer",
    "&$activeIcon": {
      color: "#f63366",
    },
    "&$completedIcon": {
      color: "#f63366",
    },
  },

  activeIcon: {},
  completedIcon: {},
}))

class StepperBar extends StreamlitComponentBase {
  state = { activeStep: 0, steps: [] }

  componentDidMount() {
    this.setState((prev, state) => ({
      steps: this.props.args.steps,
      activeStep: this.props.args.default,
    }))
  }

  onClick = (index) => {
    const { activeStep } = this.state

    if (index == activeStep + 1) {
      this.setState(
        (prev, state) => ({
          activeStep: activeStep + 1,
        }),
        () => Streamlit.setComponentValue(this.state.activeStep)
      )
    } else if (index < activeStep) {
      this.setState(
        (prev, state) => ({
          activeStep: index,
        }),
        () => Streamlit.setComponentValue(this.state.activeStep)
      )
    }
  }

  getLabelStyle = (index) => {
    const { activeStep } = this.state
    const style = {}
    if (index == activeStep) {
      style.color = "#f63366"
      style.fontStyle = "italic"
    } else if (index < activeStep) {
      style.color = "#f63366"
      style.fontWeight = "bold"
    } else {
      style.color = "grey"
    }
    return style
  }

  render = () => {
    let { classes } = this.props

    const { activeStep } = this.state
    const steps = this.state.steps

    return (
      <div className={classes.root}>
        <Stepper
          activeStep={activeStep}
          alternativeLabel
          className={classes.root}
        >
          {steps.map((label, index) => (
            <Step key={label} onClick={() => this.onClick(index)}>
              <StepLabel
                StepIconProps={{
                  classes: {
                    cursor: "pointer",

                    root: classes.icon,
                    active: classes.activeIcon,
                    completed: classes.completedIcon,
                  },
                }}
              >
                <p style={this.getLabelStyle(index)}>{label}</p>
              </StepLabel>
            </Step>
          ))}
        </Stepper>
      </div>
    )
  }
}

export default withStreamlitConnection(withStyles(styles)(StepperBar))
