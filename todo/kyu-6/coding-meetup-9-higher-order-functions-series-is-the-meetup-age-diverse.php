<?php

// https://www.codewars.com/kata/coding-meetup-number-9-higher-order-functions-series-is-the-meetup-age-diverse

function is_age_diverse(array $a): bool
{
    $withoutUnder13 = array_filter($a, function (array $developer) {
        return $developer['age'] >= 13;
    });
    $ageGroups = array_map(function (int $age) {
        return (int) floor($age / 10);
    }, array_column($a, "age"));

    return (count($ageGroups) === 10);
}