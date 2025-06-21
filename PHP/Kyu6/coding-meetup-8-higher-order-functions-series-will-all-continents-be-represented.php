<?php

// https://www.codewars.com/kata/coding-meetup-number-8-higher-order-functions-series-will-all-continents-be-represented

function all_continents(array $a): bool
{
    $expected = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania',];
    $actual = array_unique(array_column($a, 'continent'));

    return count(array_intersect($expected, $actual)) == count($expected);
}