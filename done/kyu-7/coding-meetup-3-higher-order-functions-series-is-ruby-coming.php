<?php

// https://www.codewars.com/kata/coding-meetup-number-3-higher-order-functions-series-is-ruby-coming/train/php

function is_ruby_coming(array $a): bool
{
    return count(array_filter($a, function (array $developer) {
        return ($developer['language'] === 'Ruby');
    })) > 0;
}