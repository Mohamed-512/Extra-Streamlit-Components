import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React from 'react'

import Cookies from 'universal-cookie';
/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class CookieManager extends StreamlitComponentBase<State> {
  state = {}
  componentDidMount = ()=>{
    Streamlit.setComponentReady()
  
    this.state['cookies']= new Cookies(); 
    
    const { args } = this.props

    const method = args["method"]
    const cookie = args["cookie"]
    const value = args["value"]
    const expires_at = args["expires_at"]

    let output = null

    switch (method) {
      case "set":
        output = this.setCookie(cookie, value, expires_at)
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

    Streamlit.setComponentValue(output)
  }

  render = () => {
    return <div></div>
  }

  setCookie = (cookie, value, expires_at) => {
    const { cookies } = this.state
    cookies.set(cookie, value, { path: "/", samesite: "strict", expires: new Date(expires_at) })
    return true
  }

  getCookie = (cookie) => {
    const { cookies } = this.state
    const value = cookies.cookies[cookie]
    return value
  }

  deleteCookie = (cookie) => {
    const { cookies } = this.state
    cookies.remove(cookie, { path: "/", samesite: "strict" })
    return true
  }

  getAllCookies = () => {
    const { cookies } = this.state
    return cookies.getAll()
  }
}

export default withStreamlitConnection(CookieManager)
