# https://www.codewars.com/kata/a-function-within-a-function/train/elixir

defmodule Fnwithfn do
  def always(n), do: fn -> n end
end
