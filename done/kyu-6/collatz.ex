# https://www.codewars.com/kata/collatz/train/elixir

defmodule Collatz do
  defp _collatz(1), do: [1]
  defp _collatz(n) when rem(n, 2) == 0, do: [n] ++ (n |> div(2) |> _collatz())
  defp _collatz(n), do: [n] ++ ((3 * n + 1) |> _collatz())
  def collatz(n), do: _collatz(n) |> Enum.join("->")
end

IO.inspect(Collatz.collatz(1))
IO.inspect(Collatz.collatz(2))
IO.inspect(Collatz.collatz(3))
IO.inspect(Collatz.collatz(4))
