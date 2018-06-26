# https://www.codewars.com/kata/miles-per-gallon-to-kilometers-per-liter/train/elixir

defmodule Converter do
  def convert(mpg) do
    (mpg / 2.8248105315) |> Float.round(2)
  end
end
