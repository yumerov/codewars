# https://www.codewars.com/kata/vowel-count/train/elixir

defmodule VowelCount do
  def get_count(str) do
    vowels = ["a", "e", "i", "o", "u"]

    str
    |> String.downcase()
    |> String.split("")
    |> Enum.filter(fn letter -> Enum.member?(vowels, letter) end)
    |> length()
  end
end
