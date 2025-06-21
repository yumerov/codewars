# https://www.codewars.com/kata/how-good-are-you-really/train/elixir

defmodule Detector do
  def better_than_average(class_points, your_points) do
    avg = Enum.sum(class_points) / length(class_points)
    avg < your_points
  end
end
