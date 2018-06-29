# https://www.codewars.com/kata/reverse-and-invert/train/elixir

defmodule ReverseInverter do
  defp revert(0), do: 0

  defp revert(number) do
    number
    |> abs()
    |> Integer.digits()
    |> Enum.reverse()
    |> Enum.join()
    |> Integer.parse()
    |> elem(0)
    |> Kernel.*((-number / abs(number)) |> Kernel.trunc())
  end

  def reverse_invert(lst) do
    lst
    |> Enum.filter(fn x -> is_integer(x) end)
    |> Enum.map(fn x -> revert(x) end)
  end
end
