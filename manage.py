<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Restaurant Homepage</title>
   <style>
       .address-section{
          margin:40px auto;
          padding:20px;
          max-width:800px;
          text-align:center;
          border:1px solid #ddd;
          border-radius:12px;
          box-shadow:0 2px 6px rgba(0,0,0,0.1);
        }
        .address-section h2{
            margin-bottom:10px;
        }
        .map-center{
            width:100%;
            height:300px;
            border:none;
            border-radius:8px;
        }
    </style>
</head>
<body>
    <!--Existing Homepage Content-->

    <div class="addresss-section">
        <h2>Our Address</h2>
        <p>123 Main Street, New Delhi, India</p>

        <div class="map-container">
           <!--Google Maps Embed-->
           <iframe
             src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3500.295154759186!2d77.2167210!5m2!1sen!2sin"
             allowfullscreen=""
             loading="lazy"
             referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>
    </div>
</body>
</html>    
