<?php

// https://www.codewars.com/kata/coding-meetup-number-4-higher-order-functions-series-find-the-first-python-developer

function get_first_python(array $a): string
{
    foreach ($a as $developer) {
        if ($developer['language'] === 'Python') {
            return $developer['first_name'] . ', ' . $developer['country'];
        }
    }

    return 'There will be no Python developers';
}