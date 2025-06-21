# https://www.codewars.com/kata/formatting-decimal-places-number-0

defmodule Decimator do
  def two_decimal_places(n), do: Float.round(n, 2)
end
