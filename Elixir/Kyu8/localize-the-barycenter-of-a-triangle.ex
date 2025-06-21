# https://www.codewars.com/kata/localize-the-barycenter-of-a-triangle/train/elixir

defmodule Barycenter do
  defp sum_and_round(a, b, c), do: Float.round((a + b + c) / 3, 4)

  def bar_triang({x1, y1}, {x2, y2}, {x3, y3}) do
    {sum_and_round(x1, x2, x3), sum_and_round(y1, y2, y3)}
  end
end
