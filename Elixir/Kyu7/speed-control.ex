# https://www.codewars.com/kata/speed-control/train/elixir

defmodule Speedcontrol do
  def gps(_, [_]), do: 0
  def gps(_, []), do: 0

  def gps(seconds, distances) do
    0..(Enum.count(distances) - 2)
    |> Enum.map(fn index -> Enum.at(distances, index + 1) - Enum.at(distances, index) end)
    |> Enum.map(fn delta -> 3600 * delta / seconds end)
    |> Enum.max()
    |> Kernel.trunc()
  end
end

IO.inspect(Speedcontrol.gps(20, [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]))
