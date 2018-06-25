# https://www.codewars.com/kata/sleigh-authentication/train/elixir

defmodule SleighAuthentication do
    def authenticate?(name, password) do
        ((name == "Santa Claus") and (password == "Ho Ho Ho!"))
    end

    # def authenticate?("Santa Claus", "Ho Ho Ho!"), do: true
    # def authenticate?(_name, _password), do: false 
end