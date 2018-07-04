# https://www.codewars.com/kata/highest-scoring-word/train/elixir

defmodule Kata do
  @points [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
  ]

  def points_of_letter(letter) do
    @points |> Enum.find_index(fn x -> x == letter end) |> Kernel.+(1)
  end

  def points_of_word(word) do
    word
    |> String.graphemes()
    |> Enum.to_list()
    |> Enum.map(&points_of_letter(&1))
    |> Enum.sum()
  end

  def high(str) do
    str
    |> String.split(" ")
    |> Enum.map(&{&1, points_of_word(&1)})
    |> Map.new()
    |> Enum.max_by(fn {_, points} -> points end)
    |> elem(0)
  end
end

samples = [
  {"man i need a taxi up to ubud", "taxi"},
  {"what time are we climbing up the volcano", "volcano"},
  {"take me to semynak", "semynak"},
  {"massage yes massage yes massage", "massage"},
  {"take two bintang and a dance please", "bintang"}
]

Enum.map(samples, fn {input, output} ->
  IO.inspect(input)
  IO.inspect(Kata.high(input))
  IO.inspect(output)
  IO.inspect("")
end)
