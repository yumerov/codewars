# https://www.codewars.com/kata/rotate-for-a-max/train/elixir

defmodule Maxrot do
  defp head(digits, count, index), do: Enum.slice(digits, index, count - index)
  defp tail(digits, index), do: Enum.slice(digits, 0, index)

  def max_rot(num) do
    digits = num |> Integer.digits()
    count = digits |> Enum.count()

    0..(count - 1)
    |> Enum.map(fn index -> head(digits, count, index) ++ tail(digits, index) end)
    |> Enum.map(fn x -> x |> Enum.join() |> Integer.parse() |> elem(0) end)

    # |> Enum.max()
  end
end

# IO.inspect(Maxrot.max_rot(123))
# IO.inspect(Maxrot.max_rot(1234))
# IO.inspect(Maxrot.max_rot(56789))
IO.inspect(Maxrot.max_rot(38_458_215))
