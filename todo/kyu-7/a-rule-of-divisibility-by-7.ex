# https://www.codewars.com/kata/a-rule-of-divisibility-by-7/train/elixir

defmodule Seven do
  defp _seven(m, i) when m / 100 < 1, do: [m, i]
  defp _seven(m, i), do: _seven(Kernel.trunc(m / 10) - 2 * rem(m, 10), i + 1)
  def seven(m), do: _seven(m, 0)
end

IO.inspect(Seven.seven(371))
IO.inspect(Seven.seven(1603))
IO.inspect(Seven.seven(477_557_101))
IO.inspect(Seven.seven(477_557_102))
IO.inspect(Seven.seven(19_836_826))
