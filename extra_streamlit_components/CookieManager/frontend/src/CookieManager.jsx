import {
  Streamlit,
  ComponentProps,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { useEffect, useState } from "react"

import Cookies from "universal-cookie"

let last_output = null
const cookies = new Cookies()

const CookieManager = (props: ComponentProps) => {
  const setCookie = (cookie, value, expires_at) => {
    cookies.set(cookie, value, {
      path: "/",
      samesite: "strict",
      expires: new Date(expires_at),
    })
    return true
  }

  const getCookie = (cookie) => {
    const value = cookies.get(cookie)
    return value
  }

  const deleteCookie = (cookie) => {
    cookies.remove(cookie, { path: "/", samesite: "strict" })
    return true
  }

  const getAllCookies = () => {
    return cookies.getAll()
  }

  const { args } = props

  const method = args["method"]
  const cookie = args["cookie"]
  const value = args["value"]
  const expires_at = args["expires_at"]

  let output = null

  switch (method) {
    case "set":
      output = setCookie(cookie, value, expires_at)
      break
    case "get":
      output = getCookie(cookie)
      break
    case "getAll":
      output = getAllCookies()
      break
    case "delete":
      output = deleteCookie(cookie)
      break
    default:
      break
  }

  if (output && JSON.stringify(last_output) != JSON.stringify(output)) {
    last_output = output
    Streamlit.setComponentValue(output)
    Streamlit.setComponentReady()
  }

  useEffect(() => Streamlit.setFrameHeight())
  return <div></div>
}

export default withStreamlitConnection(CookieManager)
