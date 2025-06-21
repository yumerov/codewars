<?php

// https://www.codewars.com/kata/maximum-length-difference/train/php

function mxdiflg(array $a1, array $a2): int
{
    if (count($a1) === 0 || count($a2) === 0) {
        return -1;
    }

    $a1lengths = array_map(strlen, $a1);
    $a2lengths = array_map(strlen, $a2);
    $left = abs(min($a1lengths) - max($a2lengths));
    $right = abs(max($a1lengths) - min($a2lengths));

    return max($left, $right);
}