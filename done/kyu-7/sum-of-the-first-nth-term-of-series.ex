# https://www.codewars.com/kata/sum-of-the-first-nth-term-of-series

defmodule Series do
  def sum(0), do: "0.00"
  def sum(1), do: "1.00"

  def sum(n) do
    2..n
    |> Enum.to_list()
    |> Enum.map(fn x -> member(x) end)
    |> Enum.sum()
    |> Kernel.+(1)
    |> Float.round(2)
    |> to_string()
  end

  defp member(index), do: 1 / ((index - 1) * 3 + 1)
end
