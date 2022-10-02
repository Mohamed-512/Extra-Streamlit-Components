import React from "react"
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib"

import Step from "@material-ui/core/Step"
import StepLabel from "@material-ui/core/StepLabel"
import Stepper from "@material-ui/core/Stepper"
import { createStyles, withStyles } from "@material-ui/core/styles"

const styles = createStyles((theme) => ({
  root: {
    width: "100%",
    backgroundColor: "transparent",
  },
  icon: {
    color: "grey",
    cursor: "pointer",
    "&$activeIcon": {
      color: "var(--primary-color)",
    },
    "&$completedIcon": {
      color: "var(--primary-color)",
    },
  },

  activeIcon: {},
  completedIcon: {},
}))

class StepperBar extends StreamlitComponentBase {
  state = { activeStep: 0, steps: [], lockSequence: true }

  componentDidMount() {
    this.setState((prev, state) => ({
      steps: this.props.args.steps,
      activeStep: this.props.args.default,
      lockSequence: this.props.args.lock_sequence
    }))
  }

  onClick = (index) => {
    const { activeStep, lockSequence } = this.state

    if (lockSequence) {
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
    } else {
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
      style.color = "var(--text-color)"
      style.fontStyle = "italic"
    } else if (index < activeStep) {
      style.color = "var(--text-color)"
      style.fontWeight = "bold"
    } else {
      style.color = "grey"
    }
    return style
  }

  render = () => {
    let { classes, args: { is_vertical } } = this.props

    const { activeStep } = this.state
    const steps = this.state.steps

    return (
      <div className={classes.root}>
        <Stepper
          activeStep={activeStep}
          alternativeLabel={!is_vertical}
          className={classes.root}
          orientation={is_vertical ? "vertical" : "horizontal"}
        >
          {steps.map((label, index) => (
            <Step key={label} onClick={() => this.onClick(index)} >
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
