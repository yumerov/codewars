# https://www.codewars.com/kata/watermelon/train/elixir

defmodule Watermelon do
  require Integer
  def divide(weight) when Integer.is_even(weight) and weight > 2, do: true
  def divide(_), do: false
end
