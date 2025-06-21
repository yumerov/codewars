# https://www.codewars.com/kata/fix-your-code-before-the-garden-dies/train/elixir

defmodule Garden do
  def rain_amount(mm) when mm < 40, do: "You need to give your plant #{40 - mm}mm of water"
  def rain_amount(_), do: "Your plant has had more than enough water for today!"
end
