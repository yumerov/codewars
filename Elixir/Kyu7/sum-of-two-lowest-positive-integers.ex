# https://www.codewars.com/kata/sum-of-two-lowest-positive-integers/train/elixir

defmodule SmallSummer do
  def sum_two_smallest_numbers(numbers) do
    sorted_numbers = numbers |> Enum.sort()
    [x | rest] = sorted_numbers
    [y | _] = rest

    x + y
  end
end
