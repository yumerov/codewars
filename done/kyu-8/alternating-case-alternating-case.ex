# https://www.codewars.com/kata/alternating-case-%3C-equals-%3E-alternating-case/train/elixir

defmodule Codewars.StringUtils do
    def alter_case(str) do
        str
        |> String.split("")
        |> Enum.map(fn single_char -> swap_case(single_char) end)
        |> Enum.join("")
    end

    defp swap_case(single_char) do
        cond do
            single_char == String.downcase(single_char) -> String.upcase(single_char)
            single_char == String.upcase(single_char) -> String.downcase(single_char)
        end
    end
end