defmodule RockPaperScissors do
  def rps("rock", "scissors"), do: "Player 1 won!"
  def rps("scissors", "paper"), do: "Player 1 won!"
  def rps("paper", "rock"), do: "Player 1 won!"

  def rps("scissors", "rock"), do: "Player 2 won!"
  def rps("paper", "scissors"), do: "Player 2 won!"
  def rps("rock", "paper"), do: "Player 2 won!"

  def rps("rock", "rock"), do: "Draw!"
  def rps("scissors", "scissors"), do: "Draw!"
  def rps("paper", "paper"), do: "Draw!"
end
