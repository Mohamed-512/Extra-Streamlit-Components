import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { useEffect } from "react"
import Cookies from "universal-cookie"


const CookieManager:React.FC<ComponentProps> = (props) => {

  const cookies = new Cookies()

  const { args } = props

  const set = (cookie, val, options) => {
    const converted_options = {
      expires: new Date(options.expires),
    }
    options = { ...options, ...converted_options }
 
    cookies.set(cookie, val, options)
    return true
  }

  const getCookie = (cookie) => {
    const value = cookies.get(cookie)
    return value
  }

  const getAllCookies = () => {
    return cookies.getAll()
  }

  const deleteCookie = (cookie) => { 
    cookies.remove(cookie)
    return true
  }

  const method = args["method"]
  const cookie = args["cookie"]
  const val = args["val"]  
  const options = args["options"]
  
  
  useEffect(() => {
    let output = null
    
    switch(method) {
      case "set":
        output = set(cookie, val, options)
        break
      case "get":
        output = getCookie(cookie) 
        Streamlit.setComponentValue(output)
        Streamlit.setComponentReady()
        break
      case "getAll":
        output = getAllCookies()
        Streamlit.setComponentValue(output)
        Streamlit.setComponentReady() 
        break 
      case "delete":
        output = deleteCookie(cookie)
      default:
          break
  }}, [method, cookie, val, options]) 


  return (      
        <div style={{display:"none"}}></div>
  )
}

export default withStreamlitConnection(CookieManager)
