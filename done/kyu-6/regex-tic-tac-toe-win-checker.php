<?php

// https://www.codewars.com/kata/regex-tic-tac-toe-win-checker/train/php

function regexTicTacToeWinChecker(string $board): bool
{
    $horizontalPattern = 'x{3}.{6}|...x{3}...|.{6}x{3}';
    $verticalPattern = '(x..){3}|(.x.){3}|(..x){3}';
    $diogonalPattern = 'x...x...x|..x.x.x..';
    $patternForX = "/^({$horizontalPattern}|{$verticalPattern}|{$diogonalPattern})$/i";
    if (preg_match($patternForX, $board)) {
        return true;
    }

    $patternForO = str_replace('x', 'o', $patternForX);

    return preg_match($patternForO, $board);
}
