<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<Meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Us</title>
  <style>
    body{
        font-family:Arial,sans-serif;
        background-color:#f9f9f9;
        margin:0;
        padding:0;
    }
    .container{
        width:80%;
        max-width:800px;
        background:#fff;
        margin:50px auto;
        padding:20px;
        border-radius:8px;
        box-shadow:0px 2px 8px rgba(0,0,0,0.1);
    }
    h1{
        text-align:center;
        color:#333;
    }
    .contact-info{
        margin:20px 0;
    }
    .contact-info{
        margin:8px 0;
        font-size:16px;
        
    }
    .contact-form label{
        display:block;
        margin: 10px 0 5px;
    }
    .contact-form input,
    .contact-form textarea{
        width:100%;
        padding:8px;
        border: 1px solid #ccc;
        border-radius:4px;
    }
    .contact-form button{
        margin-top:15px;
        padding:10px 20px;
        background:#4CAF50;
        color:white;
        border:none;
        border-radius:4px;
        cursor:pointer;
    }
    .contact-form  button:hover{
        background:#45a049;
    }
</head>
<body>
<div class="container">
  <h1>Contact Us</h1>
  
  <div class="contact-info">
     <p><strong>Address:</strong>123 main street, your city, india</p>
     <p><strong>Phone:</strong>+9198765432</p>
     <p><strong>Email:</strong> contact@example.com</p>
  </div>

  <hr>
  <form class="contact-form">
     <label for="name">your name</label>
     <input type="text" id="name" placeholder="enter your name" reqiured>

     <label for="email">your email</label>
     <input type="email" id="email" placeholder="enter your email" reqired>

     <label> for ="message">your message</label>
     <textarea id="message" rows="5" placeholder="type your message here "required></textarea>

     <button type="submit">send message</button>
  </form>
</div>
</body>
</html>

 
