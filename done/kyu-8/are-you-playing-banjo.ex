# https://www.codewars.com/kata/are-you-playing-banjo/train/elixir

defmodule TalantDetector do
  def are_you_playing_banjo?(name) do
    if String.match?(name, ~r/^r/i) do
      "#{name} plays banjo"
    else
      "#{name} does not play banjo"
    end
  end
end

TalantDetector.are_you_playing_banjo?("Martin")
TalantDetector.are_you_playing_banjo?("Rartin")
