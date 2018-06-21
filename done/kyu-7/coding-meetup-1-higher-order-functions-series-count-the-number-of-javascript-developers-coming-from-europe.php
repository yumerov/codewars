<?php

// http://www.codewars.com/kata/coding-meetup-number-1-higher-order-functions-series-count-the-number-of-javascript-developers-coming-from-europe/train/php

function count_developers(array $a): int
{
    return count(array_filter($a, function (array $developer) {
        return ($developer['continent'] === 'Europe') && ($developer['language'] === 'JavaScript');
    })); 
}