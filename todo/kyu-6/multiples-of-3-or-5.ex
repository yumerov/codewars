# https://www.codewars.com/kata/multiples-of-3-or-5/train/elixir

defmodule Challenge do
  def solution(number) when number < 3, do: 0

  def solution(number) do
    1..number
    |> Enum.filter(fn x -> div(x, 3) == 0 || div(x, 5) == 0 end)
    |> Enum.sum()
  end
end
