# https://www.codewars.com/kata/convert-a-string-to-a-number/train/elixir

defmodule Numerify do
  def string_to_number(str), do: str |> Integer.parse() |> elem(0)
end
