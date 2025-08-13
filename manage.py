<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <Meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page title</title>
  <style>
    body{
        font-family:sans-serif;
        display:flex;
        min-height:100vh;
        flex-direction:column;
    }
    .content{
       flex:1;
       padding-bottom:50px;
    }
    footer{
       background-color:#333;
       color:#fff;
       text-align:center;
       padding:1rem;
       width:100%;
       margin-top:auto;    
    }
 
 </style>
   
</head>
<body>
  

 <div class="content">
  <h1>this is the main area</h1>
  <p>your page content will be displayed here,above the footer.</p>
 </div>

 <footer>
   <p>&copy; <span id="current-year"></span> Your company name. All rights reserved.
 </footer>

 <script>
   document.getElementById('current-year').textContent=newDate().getFullYear():
 </script> 
</body>
</html>

 
