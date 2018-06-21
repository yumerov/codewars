# https://www.codewars.com/kata/sum-of-positive/train/elixir

defmodule Solution do
  def positive_sum(arr) do
    Enum.sum(Enum.filter(arr, fn(x) -> x > 0 end))

    # arr
    # |> Enum.filter(fn(x) -> x >= 0 end)
    # |> Enum.sum()
  end
end