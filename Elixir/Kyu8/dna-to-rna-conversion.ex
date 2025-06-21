# https://www.codewars.com/kata/dna-to-rna-conversion/train/elixir

defmodule Convertor do
  def dna_to_rna(dna), do: String.replace(dna, "T", "U")
end
