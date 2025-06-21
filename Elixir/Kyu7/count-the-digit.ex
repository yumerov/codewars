# https://www.codewars.com/kata/count-the-digit/train/elixir

defmodule Countdigit do
  def nb_dig(n, d) do
    0..n
    |> Enum.map(fn x -> Integer.digits(x * x) end)
    |> Enum.reduce(fn x, y -> x ++ y end)
    |> Enum.count(fn x -> x == d end)
  end
end

IO.inspect(Countdigit.nb_dig(10, 1))
IO.inspect(Countdigit.nb_dig(5750, 0))
