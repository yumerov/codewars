# https://www.codewars.com/kata/plural/train/elixir

defmodule Plural do
  def plural?(1), do: false
  def plural?(1.0), do: false
  def plural?(_), do: true
end
