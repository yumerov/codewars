# https://www.codewars.com/kata/generate-range-of-integers/train/elixir

defmodule NumGenerator do
  def generate_range(min, max, step) when min < max do
    [min] ++ generate_range(min + step, max, step)
  end

  def generate_range(min, max, step), do: nil
end

IO.inspect(NumGenerator.generate_range(1, 10, 4))
