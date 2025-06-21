<?php

function in_asc_order(array $arr): bool
{
  $beforeSorting = json_encode($arr);
  sort($arr);
  $afterSorting = json_encode($arr);
  
  return ($beforeSorting === $afterSorting);
}
