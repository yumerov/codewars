# https://www.codewars.com/kata/mirror-object-tcejbo-rorrim/train/elixir

defmodule MapMirror do
  def mirror(map) do
    map
    |> Enum.map(fn {key, _} -> {key, to_string(key) |> String.reverse()} end)
    |> Map.new()
  end
end

IO.inspect(MapMirror.mirror(%{abc: nil, arara: nil}))
IO.inspect(MapMirror.mirror(%{meztwnbkqyhiolcsvxgju: nil}))
IO.inspect(MapMirror.mirror(%{"1 arara 2": nil, abc?: nil}))
