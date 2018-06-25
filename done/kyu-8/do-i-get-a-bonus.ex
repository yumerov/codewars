# https://www.codewars.com/kata/do-i-get-a-bonus

defmodule Codewars.Reward do
  def bonus_time(salary, true), do: "$#{salary * 10}"
  def bonus_time(salary, false), do: "$#{salary}"
end
