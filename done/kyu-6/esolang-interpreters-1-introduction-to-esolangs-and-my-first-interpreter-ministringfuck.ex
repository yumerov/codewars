# https://www.codewars.com/kata/esolang-interpreters-number-1-introduction-to-esolangs-and-my-first-interpreter-ministringfuck/train/elixir

defmodule MiniStringFuck do
  @moduledoc false

  def execute("", _), do: ""
  def execute("." <> tail, pointer), do: List.to_string([pointer]) <> execute(tail, pointer)
  def execute("+" <> tail, pointer), do: execute(tail, rem(pointer + 1, 256))
  def execute(command, pointer), do: command |> String.slice(1..-1) |> execute(pointer)
  def execute(command), do: execute(command, 0)
end

pluses = fn n -> String.duplicate("+", n) end

letter_H = pluses.(72) <> "."
# 71 + 20 = 101 -> "e"
letter_e = pluses.(29) <> "."

hello_world =
  letter_H <>
    letter_e <>
    pluses.(7) <>
    ".." <>
    pluses.(3) <>
    "." <>
    pluses.(189) <>
    "." <>
    pluses.(244) <>
    "." <>
    pluses.(55) <>
    "." <>
    pluses.(24) <>
    "." <> pluses.(3) <> "." <> pluses.(250) <> "." <> pluses.(248) <> "." <> pluses.(189) <> "."

hello_world_non_command_chars =
  letter_H <>
    letter_e <>
    pluses.(7) <>
    ".." <>
    pluses.(3) <>
    "." <>
    pluses.(89) <>
    "a" <>
    pluses.(100) <>
    "." <>
    pluses.(244) <>
    "." <>
    pluses.(55) <>
    "." <>
    pluses.(24) <>
    "." <> pluses.(3) <> "." <> pluses.(250) <> "." <> pluses.(248) <> "." <> pluses.(189) <> "."

IO.inspect("H")
IO.inspect(MiniStringFuck.execute(letter_H))
IO.inspect("----------")

IO.inspect("He")
IO.inspect(MiniStringFuck.execute(letter_H <> letter_e))
IO.inspect("----------")

IO.inspect("Hello, World!")
IO.inspect(MiniStringFuck.execute(hello_world))
IO.inspect("----------")

IO.inspect("Hello, World!")
IO.inspect(MiniStringFuck.execute(hello_world_non_command_chars))
