# https://www.codewars.com/kata/highest-scoring-word/train/elixir

defmodule Kata do
  def compute_points(word) do
    word
    |> String.graphemes()
    |> Enum.to_list()
  end

  def high(str) do
    str
    |> String.split(" ")
    |> compute_points()
  end
end

samples = [
  {"man i need a taxi up to ubud", "taxi"}
  # {"what time are we climbing up the volcano", "volcano"},
  # {"take me to semynak", "semynak"},
  # {"massage yes massage yes massage", "massage"},
  # {"take two bintang and a dance please", "bintang"}
]

Enum.map(samples, fn {input, output} ->
  IO.inspect(input)
  IO.inspect(Kata.high(input))
  IO.inspect(output)
  IO.inspect("")
end)
