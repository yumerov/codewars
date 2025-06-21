<?php

// https://www.codewars.com/kata/lario-and-muigi-pipe-problem/train/php

function pipeFix(array $numbers): array
{
    return range(min($numbers), max($numbers));
}