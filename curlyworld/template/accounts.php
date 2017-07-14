
<?php

if ($_POST['Login']){
  
    $username = $_GET['uname'];
    $password = $_GET['psw'];
    $email = $_GET['email']
    $filename = 'accounts.txt';
    $fp = fopen($filename, 'a+');
    fwrite ($fp, $username . "," . $password . "," $email . "\n");
    $fclose ($fp);
    echo ("account created");
    header("Location: "login.html");
    die();

    <script>location.href='accounts.txt';</script>
 } ?>
