<?php

function mukNumara($numara)
{
    $carp = 0;

    for ($i = 1; $i < $numara; $i++)
    {
        if($numara % $i == 0)
        {
            $carp = $carp + $i;
        }
    }

    return $carp == $numara;

}

$numara = 6;

if(mukNumara($numara)){
    echo "DORU BILGI MUKEMMEL NUMARA BU";
}
else{
    echo "MUKEMMEL NUMARA DEGIL";
}

?>