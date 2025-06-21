# https://www.codewars.com/kata/largest-5-digit-number-in-a-series/train/elixir

defmodule LargestInSeries do
  @spec solution(String.t()) :: integer
  def solution(digits) do
    count = 5

    0..(String.length(digits) - count)
    |> Enum.map(fn index -> String.slice(digits, index, count) end)
    |> Enum.map(fn number -> Integer.parse(number) end)
    |> Enum.max()
    |> elem(0)
  end
end
