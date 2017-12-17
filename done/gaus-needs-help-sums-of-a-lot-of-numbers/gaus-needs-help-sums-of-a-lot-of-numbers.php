<?php

function f($n = null) {
  if (!is_int($n) || $n <= 0) {
    return false;
  }

  return $n * ($n + 1) / 2;
}