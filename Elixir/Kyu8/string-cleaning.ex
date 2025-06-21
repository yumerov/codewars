# https://www.codewars.com/kata/string-cleaning

defmodule Codewars do
  require Regex

  def string_clean(s), do: Regex.replace(~r/\d/, s, "")
end
