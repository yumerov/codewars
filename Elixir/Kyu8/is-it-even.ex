# https://www.codewars.com/kata/is-it-even/train/elixir

defmodule Evenator do
  def even?(n) when is_integer(n), do: rem(n, 2) == 0
  def even?(_), do: false
end
