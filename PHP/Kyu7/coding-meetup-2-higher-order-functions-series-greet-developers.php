<?php

// https://www.codewars.com/kata/coding-meetup-number-2-higher-order-functions-series-greet-developers/train/php

function greet_developers(array $a): array
{
    return array_map(function (array $developer) {
        $developer["greeting"] = "Hi {$developer['first_name']}, what do you like the most about {$developer['language']}?";

        return $developer;
    }, $a);
}