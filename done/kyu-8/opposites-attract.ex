# https://www.codewars.com/kata/opposites-attract/train/elixir

defmodule Opposites do
  require Integer
  def inlove?(flower1, flower2), do: (flower1 + flower2) |> Integer.is_odd()
end
