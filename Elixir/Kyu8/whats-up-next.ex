# https://www.codewars.com/kata/whats-up-next/train/elixir

defmodule NextBigThing do
  def next_item(list, item) do
    index = Enum.find_index(list, fn x -> x == item end)

    if index do
      Enum.at(list, index + 1, nil)
    end
  end
end
