# https://www.codewars.com/kata/two-to-one/train/elixir

defmodule TwoToOne do
  def longest(a, b) do
    a_letters =
      a
      |> String.split("")
      |> Enum.uniq()

    b_letters =
      b
      |> String.split("")
      |> Enum.uniq()

    (a_letters ++ b_letters)
    |> Enum.uniq()
    |> Enum.sort()
    |> Enum.join("")
  end

  # a <> b |> String.graphemes |> Enum.uniq |> Enum.sort |> Enum.join
end
