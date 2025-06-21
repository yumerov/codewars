# https://www.codewars.com/kata/number-of-people-in-the-bus/train/elixir

defmodule Bus do
  def number(stops) do
    stops
    |> Enum.map(fn stop -> elem(stop, 0) - elem(stop, 1) end)
    |> Enum.sum()
  end
end
