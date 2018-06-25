# https://www.codewars.com/kata/validate-code-with-simple-regex/train/elixir

defmodule CodeValidator do
  def valid?(code) do
    first = Integer.digits(code) |> List.first()
    Enum.member?([1, 2, 3], first)
  end
end
