# https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no/train/elixir

defmodule YesOrNo do
    def boolToWord(b) do
        cond do
            b -> "Yes"
            !b -> "No"
        end
    end

    # def boolToWord(true), do: "Yes"
    # def boolToWord(false), do: "No"
end