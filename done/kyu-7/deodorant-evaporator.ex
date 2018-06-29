# https://www.codewars.com/kata/deodorant-evaporator/train/elixir

defmodule Evaporator do
  @spec evaporator(number, number, number) :: number
  def evaporator(content, evap_per_day, threshold) do
    log_of_threshold = :math.log(threshold / 100)
    log_of_evaporation = :math.log((100 - evap_per_day) / 100)
    (log_of_threshold / log_of_evaporation) |> Float.ceil() |> Kernel.trunc()
  end
end

IO.inspect(Evaporator.evaporator(10, 10, 10))
IO.inspect(Evaporator.evaporator(10, 10, 5))
