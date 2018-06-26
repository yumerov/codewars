# https://www.codewars.com/kata/lario-and-muigi-pipe-problem/train/elixir

defmodule Pipeline do
  def fix_pipe(pipes), do: Enum.min(pipes)..Enum.max(pipes) |> Enum.to_list()
end
