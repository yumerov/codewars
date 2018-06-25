# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/elixir

defmodule Shepherd do
  def count_sheeps(sheeps) do
    sheeps
    |> Enum.filter(fn x -> x end)
    |> length
  end

  # Enum.count(sheeps, fn(x) -> x end)
end
