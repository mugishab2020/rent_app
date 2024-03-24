import React, { useState } from 'react'
import "../styles/register.css"

const Register = () => {

  const [state, setState] = useState({
    email: '',
    username: '',
    password: '',
    confirmpasswords: '',
    gender: ''


  })

  const handleSignUp= ()=> {
    if (state.password !== state.confirmpasswords){
      alert('Password missmatch');
      return;
    }
      fetch('http://localhost:5000/register', {
        method:'POST'
      })
  }
  return (
     <div className='register_body'>
       <form>
        <h1>Register</h1>
        <div className="inputbox">
          <input type="email"
           placeholder='Email' 
           required 
           value={state.email}
           onChange={(e)=> {
            setState({
              ...state,
              email: e.target.value
            })
           }}
            />
          </div>
          <div className='inputbox'>
          <input type="text" 
          placeholder='Username' 
          required 
          value={state.username}
          onChange={(e)=> {
            setState({
              ...state,
              username: e.target.value
            })
          }}/>
          </div>
          <div className='inputbox'>
         <input type="password" placeholder='Password' required
           value={state.password}
           onChange={(e)=> {
             setState({
               ...state,
               password: e.target.value
             })
           }}/>
          </div>
          <div className='inputbox'>
          <input type="password"
          placeholder='Retype Password'
          value={state.confirmpasswords}
           onChange={(e)=> {
             setState({
               ...state,
               confirmpasswords: e.target.value
             })
           }} 
          required />
          </div>
          <div className="inputbox">
          
            <input type="text" name="gender"
            placeholder='Gender'
            value={state.gender}
            onChange={(e)=> {
              setState({
                ...state,
                gender: e.target.value
              })
            }}/>       
          </div>
    

        <button className='button' type='submit' onClick={()=> handleSignUp()}>Register</button>
        

       </form>
      
    </div>
  )
}

export default Register
