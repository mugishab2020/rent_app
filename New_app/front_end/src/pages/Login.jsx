import React from 'react'
import "../styles/login.css"

const Login = () => {
  return (
    <div className='login_body'>
       <form action="">
        <h1>Login</h1>
        <div className="inputbox">
          <input type="text" placeholder='Username' required />
          <div className="inputbox">
          <input type="password" placeholder='Password' required />
          </div>
        
        </div>
        <div className="remember_me">
          <label> <input type="checkbox" />Remember me</label>
          <a href="Forgot_password">Forgot password</a>
        </div>
        <button className="button" type='submit'>Login</button>
        <div className="register_link">
          <p>You don't have an account ?<a href="register">Register</a></p>
        </div>

       </form>
      
    </div>
  )
}

export default Login
