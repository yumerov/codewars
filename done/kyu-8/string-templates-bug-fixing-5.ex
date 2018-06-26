# https://www.codewars.com/kata/string-templates-bug-fixing-number-5/train/elixir

defmodule Templates do
  def build_string(args), do: "I like #{Enum.join(args, ", ")}!"
end
