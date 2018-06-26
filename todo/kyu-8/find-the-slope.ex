# https://www.codewars.com/kata/find-the-slope/train/elixir

defmodule SloppyMath do
  def slope([a, _, a, _]), do: "undefined"

  def slope([a, b, c, d]) do
    ((d - b) / (c - a))
    |> Float.ceil()
    |> Kernel.trunc()
    |> to_string()
  end
end

IO.inspect(SloppyMath.slope([16, 31, 32, 11]) == "-1")
