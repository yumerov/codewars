# https://www.codewars.com/kata/simple-fun-number-165-withdraw/train/elixir

defmodule ATM do
  def is_valid_combination?(amount, hundreds, fifties, twenties) do
    amount == hundreds * 100 + fifties * 50 + twenties * 20
  end

  def first_valid_combination(amount, max_hundreds, max_fifties, max_twenties) do
    for hundreds <- max_hundreds..0,
        fifties <- max_fifties..0,
        twenties <- 0..max_twenties do
      if is_valid_combination?(amount, hundreds, fifties, twenties) do
        throw([hundreds, fifties, twenties])
      end
    end
  end

  def withdraw(n) do
    max_hundreds = div(n, 100)
    max_fifties = div(n, 50)
    max_twenties = div(n, 20)

    try do
      first_valid_combination(n, max_hundreds, max_fifties, max_twenties)
    catch
      combination -> combination
    end
  end
end

IO.inspect(ATM.withdraw(40))
IO.inspect([0, 0, 2])
IO.inspect("-------")

IO.inspect(ATM.withdraw(60))
IO.inspect([0, 0, 3])
IO.inspect("-------")

IO.inspect(ATM.withdraw(250))
IO.inspect([2, 1, 0])
IO.inspect("-------")

IO.inspect(ATM.withdraw(260))
IO.inspect([2, 0, 3])
IO.inspect("-------")

IO.inspect(ATM.withdraw(370))
IO.inspect([3, 1, 1])
IO.inspect("-------")

IO.inspect(ATM.withdraw(10000))
IO.inspect([100, 0, 0])
IO.inspect("-------")
