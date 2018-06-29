# https://www.codewars.com/kata/two-oldest-ages-1/train/elixir

defmodule Solution do
  def two_oldest_ages(ages), do: ages |> Enum.sort() |> Enum.slice(-2, 2)
end
