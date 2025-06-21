# https://www.codewars.com/kata/are-arrow-functions-odd/train/elixir

defmodule OnlyOdd do
  require Integer
  def odds(nums), do: Enum.filter(nums, fn x -> Integer.is_odd(x) end)
end
