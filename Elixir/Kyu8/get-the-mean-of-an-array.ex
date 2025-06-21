# https://www.codewars.com/kata/get-the-mean-of-an-array/train/elixir

defmodule Calculator do
  def get_average(marks) do
    if length(marks) do
      Kernel.trunc(Enum.sum(marks) / length(marks))
    else
      0
    end
  end
end