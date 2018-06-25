# https://www.codewars.com/kata/a-needle-in-the-haystack/train/elixir

defmodule Finder do
    def find_needle(haystack) do
        index = Enum.find_index(haystack, fn x -> x == "needle" end)
        "found the needle at position #{index}"
    end
end
