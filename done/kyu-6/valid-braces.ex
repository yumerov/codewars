# https://www.codewars.com/kata/valid-braces/train/elixir

defmodule Challenge do
  @opposites %{
    "(": ")",
    ")": "(",
    "{": "}",
    "}": "{",
    "[": "]",
    "]": "["
  }
  def is_open(brace), do: Enum.member?(["(", "{", "["], brace)
  def is_close(brace), do: Enum.member?([")", "}", "]"], brace)
  def are_opposites(left, right), do: @opposites[left |> String.to_atom()] == right

  defp _valid_braces([], []), do: true
  defp _valid_braces([], _), do: false

  defp _valid_braces([current | braces], open_braces) do
    cond do
      is_open(current) ->
        _valid_braces(braces, open_braces ++ [current])

      is_close(current) ->
        cond do
          are_opposites(current, List.last(open_braces)) ->
            _valid_braces(braces, Enum.slice(open_braces, 0..-2))

          true ->
            false
        end

      true ->
        false
    end
  end

  def valid_braces(braces), do: _valid_braces(braces |> String.graphemes(), [])
end

# IO.inspect(Challenge.valid_braces("("))
# IO.inspect(Challenge.valid_braces("()"))
# IO.inspect(Challenge.valid_braces("([)"))
# IO.inspect(Challenge.valid_braces("(])"))
IO.inspect(Challenge.valid_braces("[(])"))
