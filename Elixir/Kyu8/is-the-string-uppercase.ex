# https://www.codewars.com/kata/is-the-string-uppercase/train/elixir

defmodule StringUtils do
  def upper_case?(str), do: str == String.upcase(str)
end
