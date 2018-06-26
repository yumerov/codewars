# https://www.codewars.com/kata/generate-range-of-integers/train/elixir

defmodule NumGenerator do
  defp element_at_index(index, min, step), do: min + index * step

  def generate_range(min, max, step) do
    count = Integer.floor_div(max - min, step)
    for index <- 0..count, do: element_at_index(index, min, step)
  end

  # :lists.seq(min, max, step)
  # Stream.take_every(min..max, step) |> Enum.to_list()
end

IO.inspect(NumGenerator.generate_range(1, 10, 4))
