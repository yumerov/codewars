# https://www.codewars.com/kata/toleetspeak/train/elixir

defmodule ToLeetSpeak do
  @map %{
    A: "@",
    B: "8",
    C: "(",
    E: "3",
    G: "6",
    H: "#",
    I: "!",
    L: "1",
    O: "0",
    S: "$",
    T: "7",
    Z: "2"
  }

  def translate(str) do
    str
    |> String.graphemes()
    |> Enum.map(fn x -> Map.get(@map, String.to_atom(x), x) end)
    |> Enum.join()
  end
end

IO.inspect(ToLeetSpeak.translate("LEET"))
IO.inspect(ToLeetSpeak.translate("LOREM IPSUM DOLOR SIT AMET"))
