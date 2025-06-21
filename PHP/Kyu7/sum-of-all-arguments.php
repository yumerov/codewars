<?php

// https://www.codewars.com/kata/sum-of-all-arguments/train/php

function sum(): int
{
    return array_sum(func_get_args());
}