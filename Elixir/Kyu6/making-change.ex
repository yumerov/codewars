# https://www.codewars.com/kata/making-change/train/elixir

defmodule Currency do
  @nickel 5
  @dime 10
  @quarter 25
  @half 50

  defp split(amount, base), do: {div(amount, base), rem(amount, base)}
  defp next(_, head, tail) when head == 0, do: %{} |> Map.merge(make_change(tail))
  defp next(key, head, tail), do: %{String.to_atom(key) => head} |> Map.merge(make_change(tail))

  def make_change(0), do: %{}

  def make_change(amount) when amount < @nickel, do: %{P: amount}

  def make_change(amount) when amount < @dime do
    {head, tail} = split(amount, @nickel)
    next("N", head, tail)
  end

  def make_change(amount) when amount < @quarter do
    {head, tail} = split(amount, @dime)
    next("D", head, tail)
  end

  def make_change(amount) when amount < @half do
    {head, tail} = split(amount, @quarter)
    next("Q", head, tail)
  end

  def make_change(amount) do
    {head, tail} = split(amount, @half)
    next("H", head, tail)
  end
end

IO.inspect("pennies")
IO.inspect(Currency.make_change(1))
IO.inspect(%{P: 1})
IO.inspect("--------")
IO.inspect(Currency.make_change(4))
IO.inspect(%{P: 4})
IO.inspect("--------")

IO.inspect("nickels")
IO.inspect(Currency.make_change(5))
IO.inspect(%{N: 1})
IO.inspect("--------")

IO.inspect("dimes")
IO.inspect(Currency.make_change(10))
IO.inspect(%{D: 1})
IO.inspect("--------")
IO.inspect(Currency.make_change(11))
IO.inspect(%{D: 1, P: 1})
IO.inspect("--------")
IO.inspect(Currency.make_change(16))
IO.inspect(%{D: 1, N: 1, P: 1})
IO.inspect("--------")
IO.inspect(Currency.make_change(20))
IO.inspect(%{D: 2})
IO.inspect("--------")

IO.inspect("quarters")
IO.inspect(Currency.make_change(25))
IO.inspect(%{Q: 1})
IO.inspect("--------")

IO.inspect("halfs")
IO.inspect(Currency.make_change(50))
IO.inspect(%{H: 1})
IO.inspect("--------")

IO.inspect("mixed")

IO.inspect(Currency.make_change(6))
IO.inspect(%{N: 1, P: 1})
IO.inspect("--------")

IO.inspect(Currency.make_change(15))
IO.inspect(%{D: 1, N: 1})
IO.inspect("--------")

IO.inspect(Currency.make_change(43))
IO.inspect(%{D: 1, N: 1, P: 3, Q: 1})
IO.inspect("--------")

IO.inspect(Currency.make_change(91))
IO.inspect(%{H: 1, Q: 1, D: 1, N: 1, P: 1})
IO.inspect("--------")
