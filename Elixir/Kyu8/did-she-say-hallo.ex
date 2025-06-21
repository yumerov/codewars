# https://www.codewars.com/kata/did-she-say-hallo/train/elixir

defmodule Polyglot do
  def validate_hello(greeting) do
    greetings = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    String.downcase(greeting) |> String.contains?(greetings)
  end
end

IO.inspect(Polyglot.validate_hello("hello"))
IO.inspect(Polyglot.validate_hello("Ahoj"))
IO.inspect(Polyglot.validate_hello("bien la hello hasta"))
