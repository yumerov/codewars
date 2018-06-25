# https://www.codewars.com/kata/collatz-conjecture-3n-plus-1/train/elixir

defmodule Collatz do
  defp _hotpo(1, counter), do: counter

  defp _hotpo(n, counter) do
    case rem(n, 2) do
      0 -> _hotpo(div(n, 2), counter + 1)
      1 -> _hotpo(3 * n + 1, counter + 1)
    end
  end

  def hotpo(n), do: _hotpo(n, 0)

  import Integer

  # def hotpo(1), do: 0
  # def hotpo(n) when is_odd(n), do: 1 + hotpo(3*n + 1)
  # def hotpo(n) when is_even(n), do: 1 + hotpo(div(n, 2))
end
