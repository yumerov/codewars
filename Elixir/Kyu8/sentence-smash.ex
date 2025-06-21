# https://www.codewars.com/kata/sentence-smash/train/elixir

defmodule SentenceSmasher do
  def smash(words), do: Enum.join(words, " ")
end
