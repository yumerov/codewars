# https://www.codewars.com/kata/dollars-and-cents/train/elixir

defmodule Cashier do
  def format_money(amount), do: :io_lib.format("$~.2f", [sum]) |> to_string()
end
