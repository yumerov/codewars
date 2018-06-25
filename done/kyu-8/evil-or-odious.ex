# https://www.codewars.com/kata/evil-or-odious/train/elixir

defmodule Codewars.EvilOdious do
  defp label(0), do: "It's Evil!"
  defp label(1), do: "It's Odious!"

  def evil?(n) do
    Integer.digits(n, 2)
    |> Enum.sum()
    |> rem(2)
    |> label()
  end
end
