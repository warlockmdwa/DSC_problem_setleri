<?php


$myDate = date("H:i:s");

if ($myDate >= '06:00' and $myDate <= strtotime("9:59")){
    echo "Gunaydin iyi sabahlar","<br>", "Saat su an: ", $myDate;
}
else if($myDate >= "10:00" and $myDate <= "16:59"){
    echo "Iyi gunler","<br>", "Saat su an: ", $myDate;
}

else if($myDate >= "17:00" and $myDate <= "23:00"){
    echo "Iyi aksamlar","<br>", "Saat su an: ", $myDate;
}

else{
    echo "Esenlikler dilerim";
};


?>
