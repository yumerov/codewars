# https://www.codewars.com/kata/transportation-on-vacation/train/elixir

defmodule Rent do
  def rental_car_cost(d) do
    cond do
      d < 3 -> d * 40
      d < 7 -> d * 40 - 20
      true -> d * 40 - 50
    end
  end

  # @base_amount 40
  # def rental_car_cost(d) when d in 3..6, do: d * @base_amount - 20
  # def rental_car_cost(d) when d >= 7, do: d * @base_amount - 50  
  # def rental_car_cost(d), do: d * @base_amount  
end
