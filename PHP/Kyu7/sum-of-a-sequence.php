<?php

// https://www.codewars.com/kata/sum-of-a-sequence/train/php

function sequence_sum(int $begin, int $end, int $step): int
{
    if ($begin > $end) {
        return 0;
    }
  
    echo $begin, " ", $end, " ", $step, "\n";
    if ($begin + $step > $end) {
        return $begin;
    }

    return array_sum(range($begin, $end, $step));
}