# https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/elixir

defmodule Digitizer do
    def digitize(n) do
        Enum.reverse(Integer.digits(n))
    end
end