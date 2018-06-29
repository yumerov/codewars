# https://www.codewars.com/kata/currying-functions-multiply-all-elements-in-an-array/train/elixir

defmodule Multiply_all do
  def solution([]), do: fn _ -> [] end

  def solution(numbers) do
    fn multiplier -> numbers |> Enum.map(fn number -> number * multiplier end) end
  end
end

IO.inspect(Multiply_all.solution([1, 2, 3]).(2))
