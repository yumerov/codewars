# https://www.codewars.com/kata/welcome/train/elixir

defmodule Greeter do
  @greeting %{
    "english" => "Welcome",
    "czech" => "Vitejte",
    "danish" => "Velkomst",
    "dutch" => "Welkom",
    "estonian" => "Tere tulemast",
    "finnish" => "Tervetuloa",
    "flemish" => "Welgekomen",
    "french" => "Bienvenue",
    "german" => "Willkommen",
    "irish" => "Failte",
    "italian" => "Benvenuto",
    "latvian" => "Gaidits",
    "lithuanian" => "Laukiamas",
    "polish" => "Witamy",
    "spanish" => "Bienvenido",
    "swedish" => "Valkommen",
    "welsh" => "Croeso"
  }
  def greet(language) do
    @greeting[language] || "Welcome"
  end
end
