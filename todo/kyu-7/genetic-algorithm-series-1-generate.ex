# https://www.codewars.com/kata/genetic-algorithm-series-number-1-generate/train/elixir

defmodule Genetic do
  def generate(0), do: 0

  def generate(length) do
    1..length |> Enum.map(fn _ -> Enum.random(0..1) end) |> Enum.join()
  end
end

IO.inspect(Genetic.generate(13))
