# https://www.codewars.com/kata/get-the-middle-character/train/elixir

defmodule Challenge do
  def get_middle(str) do
    count = str |> String.length()
    half = Integer.floor_div(count, 2)

    if count |> rem(2) == 0 do
      String.slice(str, half - 1, 2)
    else
      String.slice(str, half, 1)
    end
  end
end

IO.inspect(Challenge.get_middle("test"))
IO.inspect(Challenge.get_middle("testing"))
