# https://www.codewars.com/kata/leonardo-dicaprio-and-oscars/train/elixir

defmodule Oscar do
  def leo(88), do: "Leo finally won the oscar! Leo is happy"
  def leo(86), do: "Not even for Wolf of wallstreet?!"
  def leo(oscar) when oscar < 88, do: "When will you give Leo an Oscar?"
  def leo(_), do: "Leo got one already!"
end
