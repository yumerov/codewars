# https://www.codewars.com/kata/repeatit/train/elixir

defmodule Repeater do
  def repeat_it(str, n) when is_binary(str), do: String.duplicate(str, n)
  def repeat_it(_, _), do: "Not a string"
end
