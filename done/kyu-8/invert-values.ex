# https://www.codewars.com/kata/invert-values

defmodule Inverter do
  def invert(list), do: Enum.map(list, fn x -> -x end)
end
