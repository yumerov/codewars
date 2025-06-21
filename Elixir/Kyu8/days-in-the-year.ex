# https://www.codewars.com/kata/days-in-the-year/train/elixir

defmodule DateUtils do
  defp _year_days(0), do: 366
  defp _year_days(_), do: 365

  def year_days(year), do: "#{year} has #{_year_days(rem(year, 4))} days"
end
