import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React from 'react'
import { instanceOf } from "prop-types"

import { withCookies, Cookies } from "react-cookie"

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class CookieManager extends StreamlitComponentBase<State> {
  componentDidMount = ()=>{
    Streamlit.setComponentReady()

    const { args } = this.props

    const method = args["method"]
    const cookie = args["cookie"]
    const value = args["value"]
  
    let output = null

    switch (method) {
      case "set":
        output = this.setCookie(cookie, value)
        break
      case "get":
        output = this.getCookie(cookie)
        break
      case "getAll":
        output = this.getAllCookies()
        break
      case "delete":
        output = this.deleteCookie(cookie)
        break
      default:
        break
    }

    console.log(output);
    Streamlit.setComponentValue(output)
  }

  render = () => {
    return <div></div>
  }

  setCookie = (cookie, value) => {
    const { cookies } = this.props
    cookies.set(cookie, value, { path: "/", samesite: "strict" })
    return true
  }

  getCookie = (cookie) => {
    const { cookies } = this.props
    const value = cookies.cookies[cookie]
    return value
  }

  deleteCookie = (cookie) => {
    const { cookies } = this.props
    cookies.remove(cookie, { path: "/", samesite: "strict" })
    return true
  }

  getAllCookies = () => {
    const { cookies } = this.props
    return cookies.cookies
  }
}

CookieManager.propTypes = {
  cookies: instanceOf(Cookies).isRequired,
}

export default withStreamlitConnection(withCookies(CookieManager))
