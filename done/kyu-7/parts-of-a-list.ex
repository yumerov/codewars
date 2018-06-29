# https://www.codewars.com/kata/parts-of-a-list/train/elixir

defmodule Partlist do
  defp left(words, index), do: Enum.slice(words, 0..index) |> Enum.join(" ")
  defp right(words, index), do: Enum.slice(words, (index + 1)..-1) |> Enum.join(" ")

  def part_list(words) do
    0..(Enum.count(words) - 2)
    |> Enum.map(fn index -> [left(words, index), right(words, index)] end)
  end
end

IO.inspect(Partlist.part_list(["I", "wish", "I", "hadn't", "come"]))
