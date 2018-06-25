# https://www.codewars.com/kata/name-shuffler/train/elixir

defmodule Messy do
  def name_shuffler(str) do
    name_parts = String.split(str, " ")
    "#{Enum.at(name_parts, 1)} #{Enum.at(name_parts, 0)}"
  end
end
