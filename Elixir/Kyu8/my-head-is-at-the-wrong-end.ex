# https://www.codewars.com/kata/my-head-is-at-the-wrong-end/train/elixir

defmodule Codewars.Zoo do
  def fix_the_meerkat(tuple), do: {elem(tuple, 2), elem(tuple, 1), elem(tuple, 0)}
  #   def fix_the_meerkat({t, b, h}), do: {h, b, t}
end
