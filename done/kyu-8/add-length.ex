# https://www.codewars.com/kata/add-length/train/elixir

defmodule Marker do
  def add_length(str) do
    str
    |> String.split([" "])
    |> Enum.map(fn x -> "#{x} #{String.length(x)}" end)
  end
end

Marker.add_length("apple ban")
