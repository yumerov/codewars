# https://www.codewars.com/kata/regexp-basics-is-it-a-digit/train/elixir

defmodule StringUtils do
  def digit?(s), do: String.match?(s, ~r/^\d$/) and String.length(s) == 1
end
