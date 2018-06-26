# https://www.codewars.com/kata/remove-the-time/train/elixir

defmodule Datemizer do
  def shorten_to_date(datetime), do: String.replace(datetime, ~r/,\s\d{1,2}(a|p)m/, "")
end
