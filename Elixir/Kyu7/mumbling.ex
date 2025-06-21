# https://www.codewars.com/kata/mumbling/train/elixir

defmodule Mumbling do
  defp duplicate(char, count) do
    for index <- 1..count do
      cond do
        index == 1 -> char |> String.upcase()
        true -> char
      end
    end
    |> Enum.join("")
  end

  def accum(str) do
    downcased_str = str |> String.downcase()
    count = String.length(str)

    for index <- 0..(count - 1) do
      downcased_str
      |> String.at(index)
      |> duplicate(index + 1)
    end
    |> Enum.join("-")
  end
end

IO.inspect(Mumbling.accum("abcd"))
# IO.inspect(Mumbling.accum("RqaEzty"))
# IO.inspect(Mumbling.accum("cwAt"))
