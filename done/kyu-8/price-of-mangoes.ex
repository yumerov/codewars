# https://www.codewars.com/kata/price-of-mangoes/train/elixir

defmodule Solution do
  def mango(quantity, price), do: (Integer.floor_div(quantity, 3) * 2 + rem(quantity, 3)) * price
end
