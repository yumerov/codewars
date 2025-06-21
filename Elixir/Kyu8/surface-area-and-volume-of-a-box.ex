# https://www.codewars.com/kata/surface-area-and-volume-of-a-box/train/elixir

defmodule Measurer do
  defp area(w, h, d), do: 2 * (w * h + h * d + d * w)
  defp volume(w, h, d), do: w * h * d
  def get_size(w, h, d), do: {area(w, h, d), volume(w, h, d)}
end
