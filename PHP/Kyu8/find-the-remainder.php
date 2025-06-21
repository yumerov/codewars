<?php

function remainder(int $a, int $b)
{
    $min = min(abs($a), abs($b));
    
    if ($min === 0) {
      return null;
    }
    
    return max($a, $b) % $min;
}
