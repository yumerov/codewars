# https://www.codewars.com/kata/anagram-detection/train/elixir

defmodule Anagram do
  def simplify(str), do: str |> String.downcase() |> String.graphemes() |> Enum.sort()
  def anagram?(a, b), do: simplify(a) == simplify(b)
end
