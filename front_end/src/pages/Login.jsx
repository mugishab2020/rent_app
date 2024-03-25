import React, { useState } from 'react'
import "../styles/login.css"

const Login = () => {
  const [state, setState] = useState({
    username: '',
    password: ''
    });
    const handleChange = (e) => {
      const { name, value } = e.target;
      setState({
        ...state,
        [name]: value
      });
    };

    const handleSubmit = (e) => {
      e.preventDefault();
      fetch('http://127.0.0.1:5000/login',{
        method: ['GET'],
        headers: {
          'content-type': 'application/json',
        }, 
        body: JSON.stringify(state)})
        .then(response => response.json())
        .then(data => {
          console.log('Login response:', data); 
          setState({
            username: '',
            password: ''
          });
        })
        .catch(error => {
          console.error('Error:', error); 
        });
    };
    
  return (
    <div className='login_body'>
       <form action="/login" 
       onSubmit={handleSubmit} 
       method='POST'>
        <h1>Login</h1>
        <div className="inputbox">
          <input type="text"
          placeholder='Username'
          name='username'
          value={useState.username}
          onChange={handleChange}
           required />
          </div>

        <div className="inputbox">
          <input type="password"
          name="password"
          placeholder='Password'
          value={useState.password}
          onChange={handleChange}
          required  />
          
        
        </div>
        <div className="remember_me">
          <label> <input type="checkbox" />Remember me</label>
          <a href="Forgot_password">Forgot password</a>
        </div>
        <button className="button" type='submit' onClick={()=> handleSubmit()}>Login</button>
        <div className="register_link">
          <p>You don't have an account ?<a href="register">Register</a></p>
        </div>

       </form>
      
    </div>
  )
}

export default Login