# https://www.codewars.com/kata/stringy-strings/train/elixir

defmodule OneZeroSequencer do
    require Integer
    def stringy(size) do
        body(size) <> tail(size)
    end

    defp body(size) do
        String.duplicate("10", Integer.floor_div(size, 2))
    end

    defp tail(size) do
        case Integer.is_even(size) do
           true -> ""
           false -> "1"
        end
    end
end

OneZeroSequencer.stringy(3)
OneZeroSequencer.stringy(4)