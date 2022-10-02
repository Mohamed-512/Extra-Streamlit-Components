import React, { ComponentProps, ReactNode } from "react"
import ScrollMenu from "react-horizontal-scrolling-menu"
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib"

interface State {
  numClicks: number
  selectedId: number
}

interface MenuItem {
  id: number
  title: string
  description: string
}

class TabBar extends StreamlitComponentBase<State> {
  public state = { numClicks: 0, selectedId: 1, list: [] }

  constructor(props: ComponentProps<any>) {
    super(props)
    this.state.list = this.props.args["data"]
    this.state.selectedId = this.props.args["selectedId"]
  }

  MenuItem = ({ item, selectedId }: { item: MenuItem; selectedId: number }) => {

    return (
      <div className={`menu-item ${selectedId == item.id ? "active" : ""}`}>
        <div>{item.title}</div>
        <div style={{ fontWeight: "normal", fontStyle: "italic" }}>
          {item.description}
        </div>
      </div>
    )
  }

  Menu(list: Array<MenuItem>, selectedId: number) {
    return list.map((item) => (
      <this.MenuItem item={item} selectedId={selectedId} key={item.id} />
    ))
  }
  Arrow = ({ text, className }: { text: string; className: string }) => {
    return <div className={className}>{text}</div>
  }

  ArrowLeft = this.Arrow({ text: "<", className: "arrow-prev" })
  ArrowRight = this.Arrow({ text: ">", className: "arrow-next" })

  public render = (): ReactNode => {
    return (
      <div>
        <ScrollMenu
          alignCenter={false}
          data={this.Menu(this.state.list, this.state.selectedId)}
          wheel={true}
          scrollToSelected={true}
          selected={`${this.state.selectedId}`}
          onSelect={this.onSelect}
        />
        <hr
          style={{
            borderColor: "var(--primary-color)",
          }}
        />
      </div>
    )
  }

  onSelect = (id: any) => {
    this.setState(
      (state, props) => {
        return { selectedId: id }
      },
      () => Streamlit.setComponentValue(id)
    )
  }
}

export default withStreamlitConnection(TabBar)
