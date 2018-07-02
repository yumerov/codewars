# https://www.codewars.com/kata/pentabonacci/train/elixir

defmodule Pentabonacci do
  require Integer

  def count_odd_pentaFib(n) when n <= 7, do: 1
  def count_odd_pentaFib(n), do: div(n - 7, 6) * 2 + 2
end
