<?php

function asal($sayi){
  if ($sayi == 1)
  {
    return 0;
  }

  for ($i = 2; $i <= $sayi/2; $i++)
  {

    if($sayi % $i == 0){
      return 0;
    }

  }

  return 1;
}


$sayi = 47;
$kontrol = 1;

$sayac = asal($sayi);
if ($sayac == $kontrol){
  echo "ASAL";
}
else{
  echo "asal degil";
}

?>
