# https://www.codewars.com/kata/printer-errors/train/elixir

defmodule Printererror do
  def printer_error(colors) do
    errors =
      colors
      |> String.graphemes()
      |> Enum.count(fn x -> String.match?(x, ~r/[^a-m]/i) end)

    "#{errors}/#{String.length(colors)}"
  end
end

IO.inspect(Printererror.printer_error("aaabbbbhaijjjm"))
IO.inspect(Printererror.printer_error("aaaxbbbbyyhwawiwjjjwwm"))
