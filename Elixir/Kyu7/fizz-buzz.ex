# https://www.codewars.com/kata/fizz-buzz/train/elixir

defmodule FizzBuzz do
  defp label(x) when rem(x, 15) == 0, do: "FizzBuzz"
  defp label(x) when rem(x, 3) == 0, do: "Fizz"
  defp label(x) when rem(x, 5) == 0, do: "Buzz"
  defp label(x), do: x
  def fizzbuzz(n), do: 1..n |> Enum.map(fn x -> label(x) end)
end
