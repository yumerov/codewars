# https://www.codewars.com/kata/the-if-function

defmodule Conditional do
  def _if(bool, fthen, felse) do
    if bool, do: fthen.(), else: felse.()
  end

  # def _if(nil, _, felse), do: felse.()
  # def _if(false, _, felse), do: felse.()
  # def _if(_, fthen, _), do: fthen.()
end
