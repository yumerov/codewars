<?php

// https://www.codewars.com/kata/coding-meetup-number-9-higher-order-functions-series-is-the-meetup-age-diverse

function is_age_diverse(array $a): bool
{
    $groups = array_unique(array_map(function (int $age) {
        return (int) floor($age / 10);
    }, array_column($a, "age")));

    return (count($groups) === 10);
}