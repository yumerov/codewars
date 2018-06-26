# https://www.codewars.com/kata/smallest-unused-id/train/elixir

defmodule Order do
  defp _next_id([], ids), do: List.last(ids) + 1
  defp _next_id(diff, _), do: List.first(diff)

  def next_id(ids) do
    unique_ids = ids |> Enum.uniq() |> Enum.sort()

    0..List.last(unique_ids)
    |> Enum.to_list()
    |> Kernel.--(unique_ids)
    |> _next_id(unique_ids)
  end
end
