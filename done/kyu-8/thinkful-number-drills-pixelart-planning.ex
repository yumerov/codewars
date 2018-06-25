# https://www.codewars.com/kata/thinkful-number-drills-pixelart-planning/train/elixir

defmodule Wall do
  def is_divisible(wall_length, pixel_size), do: rem(wall_length, pixel_size) == 0
end
