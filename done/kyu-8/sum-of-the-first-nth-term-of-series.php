<?php

// https://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/train/php

function series_sum(int $n): float
{
    $s = 0;
    for ($i = 1; $i <= $n; $i++) { 
        $s += 1 / (($i - 1) * 3 + 1);
    }

    return round($s, 2);
}