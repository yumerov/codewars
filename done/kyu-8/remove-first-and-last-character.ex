# https://www.codewars.com/kata/remove-first-and-last-character/train/elixir

defmodule Solution do
    def remove_chars(s), do: String.slice s, 1, String.length(s) - 2
end