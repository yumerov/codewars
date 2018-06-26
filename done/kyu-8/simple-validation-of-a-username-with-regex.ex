# https://www.codewars.com/kata/simple-validation-of-a-username-with-regex/train/elixir

defmodule UserValidator do
  def valid?(username) do
    String.match?(username, ~r/^[a-z0-9_]{4,16}$/) && !String.contains?(username, "\n")
  end
end

IO.inspect(UserValidator.valid?("asd43_34\n"))
