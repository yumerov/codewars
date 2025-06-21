# https://www.codewars.com/kata/check-passwords/train/elixir

defmodule Password do
  def check(password, hashed_password) do
    :sha256
    |> :crypto.hash(password)
    |> Base.encode16()
    |> Kernel.==(hashed_password)
  end
end

IO.inspect(Password.check("", ""))

IO.inspect(
  Password.check("anything", "CF329313EBB04CD2A6440547EC374C5A8EF601C82862251782EB03843DED6BEA")
)

IO.inspect(
  Password.check(
    "correct.horse.battery.staple",
    "CF329313EBB04CD2A6440547EC374C5A8EF601C82862251782EB03843DED6BEA"
  )
)
