<?php

// https://www.codewars.com/kata/coding-meetup-number-5-higher-order-functions-series-prepare-the-count-of-languages/train/php

function count_languages(array $a): array
{
    return array_count_values(array_column($a, "language"));
}