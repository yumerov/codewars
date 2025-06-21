# https://www.codewars.com/kata/remove-exclamation-marks/train/elixir

defmodule Codewars do
  def remove_exclamation_marks(s), do: s |> String.replace(~r/!/, "")
end
