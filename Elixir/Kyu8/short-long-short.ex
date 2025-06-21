# https://www.codewars.com/kata/short-long-short/train/elixir

defmodule ShortLongShort do
  def solution(a, b) do
    cond do
      String.length(a) > String.length(b) -> b <> a <> b
      true -> a <> b <> a
    end
  end
end
