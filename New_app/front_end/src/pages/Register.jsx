import React from 'react'
import "../styles/register.css"

const Register = () => {
  return (
     <div className='register_body'>
       <form action="">
        <h1>Register</h1>
        <div className="inputbox">
          <input type="text" placeholder='Email' required />
          </div>
          <div className='inputbox'>
          <input type="text" placeholder='Username' required />
          </div>
          <div className='inputbox'>
          <input type="password" placeholder='Password' required />
          </div>
          <div className='inputbox'>
          <input type="password" placeholder='Retype Password' required />
          </div>
          <div className="input">
          <label>
            <input type="radio" name="gender" value="male" checked/>Male
          </label>
          <label>
            <input type="radio" name="gender" value="female"/>Female
          </label>
          </div>
    

        <button className='button' type='submit'>Register</button>
        

       </form>
      
    </div>
  )
}

export default Register
