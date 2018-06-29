# https://www.codewars.com/kata/rectangle-into-squares/train/elixir

defmodule Rec2sq do
  defp _squares_in_rect(side, side), do: [side]

  defp _squares_in_rect(length, width) do
    min_side = min(width, length)
    diff_side = abs(length - width)
    [min_side] ++ _squares_in_rect(min_side, diff_side)
  end

  def squares_in_rect(side, side), do: nil

  def squares_in_rect(length, width), do: _squares_in_rect(length, width)
end

IO.inspect(Rec2sq.squares_in_rect(5, 5))
IO.inspect(Rec2sq.squares_in_rect(5, 3))
IO.inspect(Rec2sq.squares_in_rect(3, 5))
