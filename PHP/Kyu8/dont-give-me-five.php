<?php

// https://www.codewars.com/kata/dont-give-me-five/train/php

function dont_give_me_five(int $start, int $end): int
{
    $counter = 0;
    for ($index = $start; $index <= $end; $index++) { 
        if (strpos((string) $index, '5') === false) {
            $counter++;
        }
    }

    return $counter;
}