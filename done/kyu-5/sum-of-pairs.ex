# https://www.codewars.com/kata/sum-of-pairs/train/elixir

defmodule SumOfPairs do
  defp iterate(ints, sum) do
    limit = ints |> Enum.count() |> Kernel.-(1)

    for i <- 0..(limit - 1),
        j <- (i + 1)..limit do
      {a, b} = {Enum.at(ints, i), Enum.at(ints, j)}

      if a + b == sum, do: throw({a, b})
    end
  end

  @doc """
  Finds the first pair of ints as judged by the index of the second value.
  iex> sum_pairs( [ 10, 5, 2, 3, 7, 5 ], 10 )
  { 3, 7 }
  """
  @spec sum_pairs([integer], integer) :: {integer, integer} | nil
  def sum_pairs(ints, sum) do
    try do
      iterate(ints, sum)
      nil
    catch
      pair -> pair
    end
  end
end

IO.inspect(SumOfPairs.sum_pairs([1, 4, 8, 7, 3, 15], 8))
IO.inspect({1, 7})
IO.inspect("-----------")
IO.inspect(SumOfPairs.sum_pairs([1, -2, 3, 0, -6, 1], -6))
IO.inspect({0, -6})
IO.inspect("-----------")
IO.inspect(SumOfPairs.sum_pairs([5, 9, 13, -3], 10))
IO.inspect({13, -3})
IO.inspect("-----------")
IO.inspect(SumOfPairs.sum_pairs([20, -13, 40], -7))
IO.inspect(nil)
IO.inspect("-----------")
IO.inspect(SumOfPairs.sum_pairs([10, 5, 2, 3, 7, 5], 10))
IO.inspect({3, 7})
IO.inspect("-----------")
