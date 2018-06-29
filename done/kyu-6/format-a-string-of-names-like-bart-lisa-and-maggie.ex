# https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/train/elixir

defmodule People do
  def list([]), do: ""
  def list([person]), do: person.name
  def list([person1, person2]), do: "#{person1.name} & #{person2.name}"

  def list(people) do
    people
    |> Enum.slice(0..-3)
    |> Enum.map(fn person -> person.name end)
    |> Enum.join(", ")
    |> Kernel.<>(", ")
    |> Kernel.<>(people |> Enum.slice(-2..-1) |> list())
  end
end

IO.inspect(
  People.list([
    %{name: "Bart"},
    %{name: "Lisa"},
    %{name: "Maggie"},
    %{name: "Homer"},
    %{name: "Marge"}
  ])
)

IO.inspect(People.list([%{name: "Bart"}, %{name: "Lisa"}, %{name: "Maggie"}]))
IO.inspect(People.list([%{name: "Bart"}, %{name: "Lisa"}]))
IO.inspect(People.list([%{name: "Bart"}]))
IO.inspect(People.list([]))
