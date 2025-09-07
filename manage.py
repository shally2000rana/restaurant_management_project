<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Menu Search</title>
   <style>
      body{
      font-family:Arial, sans-serif;
      padding:20px;
      background:#f9f9f9;
     }
      h1{
      text-align:center;
     }
      #searchBar{
       width:100%;
       padding:10px;
       margin:20px 0;
       font-size:16px;
       border:1px solid #ccc;
       border-radius:8px;
      }
      ul{
      padding:10px;
      margin:5px 0;
      background:#fff;
      border-radius:6px;
      box-shadow:0 2px 4px rgba(0,0,0,0.1);
       }
    </style>
</head>
<body>
   <h1>Our Menu</h1>
   <input type="text" id="searchBar" placeholder="Search menu items ...">

   <ul id="menuList">
     <li>Pizza Margherita</li>
     <li>Veggie Burger</li>
     <li>Caesar Salad</li>
     <li>Pasta Alfredo</li>
     <li>Grilled Sandwich</li>
     <li>Tomato Soup</li>
     <li>French Fries</li>
    </ul>
    <script>
      const searchBar=document.getElementById('searchBar');
      const menuList=document.getElementById('menuList');
      const items=menuList.getElementById('li');

      searchBar.addEventListener('keyup',function(){
        const filter=searchBar.value.toLowerCase();
        for(let i=0; i< items.length; i++){
           const text=items[i].textContent.toLowerCase();
           items[i].style.display=text.includes(filter) ? '' : 'none';
        }
      });
    </script>
</body>
</html>
