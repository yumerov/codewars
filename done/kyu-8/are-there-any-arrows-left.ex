# https://www.codewars.com/kata/are-there-any-arrows-left/train/elixir

defmodule Quiver do
  def any_arrows?(arrows) do
    arrows
    |> Enum.filter(fn arrow -> !arrow["damaged"] end)
    |> Enum.empty?()
    |> Kernel.!()
  end

  # recursive solution
  # def any_arrows?([]), do: false
  # def any_arrows?([%{"damaged" => true} | rest]), do: any_arrows?(rest)
  # def any_arrows?(_), do: true
end

IO.inspect(
  Quiver.any_arrows?([%{"range" => 5}, %{"range" => 10, "damaged" => true}, %{"damaged" => true}]) ==
    true
)

IO.inspect(Quiver.any_arrows?([%{"range" => 5, "damaged" => false}]) == true)

IO.inspect(
  Quiver.any_arrows?([%{"range" => 10, "damaged" => true}, %{"damaged" => true}]) == false
)
