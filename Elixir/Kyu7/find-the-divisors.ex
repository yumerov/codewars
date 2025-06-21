# https://www.codewars.com/kata/find-the-divisors/train/elixir

defmodule FindTheDivisors do
  def divisors(2), do: [2]

  def divisors(integer) do
    limit = (integer / 2) |> Kernel.trunc() |> Kernel.+(1)

    divisors =
      2..limit
      |> Enum.to_list()
      |> Enum.filter(fn x -> rem(integer, x) == 0 end)

    if Enum.empty?(divisors) do
      "#{integer} is prime"
    else
      divisors
    end
  end
end

IO.inspect(FindTheDivisors.divisors(12))
