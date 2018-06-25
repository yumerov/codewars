# https://www.codewars.com/kata/triple-trouble-2/train/elixir

defmodule Codewars.WeirdString do
  alias String.at(), do: at

  def triple_trouble(one, two, three) do
    0..(String.length(one) - 1)
    |> Enum.map(fn i -> at(one, i) <> at(two, i) <> at(three, i) end)
    |> Enum.join()
  end
end
